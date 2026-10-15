import json
import os
from pathlib import Path
import subprocess
import sys

def test_stdio_uses_utf8_even_with_legacy_windows_encoding():
    request={'jsonrpc':'2.0','id':1,'method':'tools/call',
             'params':{'name':'model_rename','arguments':{'title':'Turbina · versión 日本語'}}}
    script='from daedalus import mcp; mcp.call=lambda name,args: args; mcp.main()'
    result=subprocess.run([sys.executable,'-c',script],input=(json.dumps(request,ensure_ascii=False)+'\n').encode('utf-8'),
                          stdout=subprocess.PIPE,stderr=subprocess.PIPE,cwd=Path(__file__).resolve().parents[1],
                          env=dict(os.environ,PYTHONIOENCODING='cp1252'),check=True)
    response=json.loads(result.stdout.decode('utf-8'))
    assert json.loads(response['result']['content'][0]['text'])==request['params']['arguments']
