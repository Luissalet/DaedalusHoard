# Daedalus's Hoard

Generación local de modelos 3D desde imágenes, con una pasada de refinado opcional y comparación de versiones.

Importa PNG, JPG o WebP, genera a 512 o 1024 y conserva el modelo completo. El visor permite inspeccionar materiales o geometría, comparar un refinado con su original con cámaras enlazadas y descargar GLB, STL o PLY indicando el tamaño del lado mayor. La biblioteca conserva trabajos, errores y versiones entre sesiones. Cancelar un trabajo no borra sus originales.

El refinado crea otra geometría y puede perder huecos o detalles. En la prueba mecánica del 15-10-2026, DetailGen3D no superó al original de TRELLIS.2, tampoco con 8192 latentes. Está disponible para comparar, sin sustituir el original. Los materiales del refinado se transfieren de la generación si se selecciona «Conservar aspecto»; no son una nueva síntesis de texturas. Las mallas abiertas requieren preparación antes de imprimir; no hay reparación, retopología ni rigging automáticos.

## Ejecución

En este equipo, abre `launch.cmd` o Daedalus en Hoard Hub. Puerto predeterminado: http://127.0.0.1:8830. El entorno propio está en `D:/LocalAI/HoardStorage/daedalus-runtime`; los pesos, en `D:/LocalAI/HoardStorage/daedalus-models`. La carpeta puede cambiarse en «4 gráficas». El programa no descarga pesos al generar.

El motor incorporado vive en `daedalus/geometry`. No inicia ComfyUI ni el programa de otro proyecto. Requiere las cuatro NVIDIA del equipo: físicas 1, 2 y 3 (16 GB) y 0 (12 GB). Distribuye las capas del generador en 8/8/8/6 y las del refinador en 6/6/6/6. Es reparto secuencial de capas; no suma las memorias como si fueran una tarjeta ni promete acelerar frente a una GPU mayor. El Hub concede los cuatro leases antes de cargar. Si están ocupadas, espera y se puede cancelar. El LLM global de las Sparks sigue siendo el servicio de Faustus y del copilot común.

Para preparar otro entorno, instala Python 3.13, PyTorch CUDA 12.8 y las dependencias de `requirements.txt` (el índice oficial de PyTorch debe proporcionar los paquetes `+cu128`). `hoard-link` es la biblioteca compartida de la familia. Coloca los archivos con la estructura descrita en `docs/MODELS.md`. `tools/prepare_models.py` es una ayuda de instalación desde los archivos locales de investigación de este equipo; no forma parte de la ejecución del motor.

## Archivos y unidades

Cada trabajo guarda parámetros, progreso, geometría original, materiales, vista simplificada y resultado en una carpeta independiente. La base SQLite está en `data/daedalus.db`. `DAEDALUS_DATA_DIR` permite instancias de pruebas separadas; no compartas la misma carpeta con dos servidores. Los trabajos activos se marcan interrumpidos al recuperar una sesión; los que aún estaban en cola vuelven a la cola.

El tamaño no se deduce de una imagen. El lado mayor indicado al exportar se escribe en metros para GLB y en milímetros para STL/PLY. GLB permite elegir la vista con materiales o la geometría completa. La copia completa conserva geometría y color de vértices; el aspecto PBR detallado está en la vista con materiales. STL no contiene color. PLY conserva el color de vértices. Escalar una exportación no altera los archivos originales.

## API y MCP

`python -m daedalus` inicia la aplicación. `python -m daedalus.mcp` expone 11 herramientas por stdio contra esa misma API: importar imagen, generar, refinar, listar/leer/cancelar trabajos, consultar versiones, renombrar, exportar, consultar motores y configurar su carpeta. Generar y refinar devuelven un ID de trabajo asíncrono; `job_get` lee el estado real. Configuración MCP en `faustus-plugin.json`; `DAEDALUS_URL` selecciona la instancia y `DAEDALUS_TOKEN_FILE` su token local. Los agentes y la interfaz utilizan la misma cola y los mismos datos.

## Verificación

Pruebas CPU: `python -m pytest`. Cubren conservación de versiones, unidades exportadas, cancelación y eventos tardíos, recuperación, instancia única, paridad API/herramientas y operaciones geométricas. Las pruebas reales de generación/refinado por MCP y las comprobaciones de navegador tienen sus recibos en las carpetas privadas de investigación de la tarea Ágora622; no se ejecutan durante la suite CPU. Los resultados y límites del experimento comparativo anterior están en `docs/EXPERIMENT.md`.

Código GPL-3.0; los pesos y componentes tienen sus propias licencias. Véase `THIRD_PARTY.md` antes de redistribuirlos.
