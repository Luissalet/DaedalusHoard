import torch
from daedalus.geometry.surface_vae import SparseConv3d,SparseTensor
from daedalus.geometry.ops import apply_rope1,optimized_attention

def test_sparse_pointwise_convolution_matches_dense_linear():
    coords=torch.tensor([[0,0,0,0],[0,0,0,1],[0,1,0,0]],dtype=torch.int32)
    features=torch.tensor([[1.,2.],[3.,4.],[5.,6.]])
    tensor=SparseTensor(features,coords)
    model=SparseConv3d(2,3,1)
    with torch.no_grad():
        model.weight.copy_(torch.tensor([[1.,0.],[0.,1.],[1.,1.]]).reshape(3,1,1,1,2))
        model.bias.fill_(.5)
    result=model(tensor)
    expected=torch.tensor([[1.5,2.5,3.5],[3.5,4.5,7.5],[5.5,6.5,11.5]])
    torch.testing.assert_close(result.feats,expected)
    torch.testing.assert_close(result.coords,coords)

def test_attention_head_layout_and_rotary_identity():
    q=torch.randn(2,3,4,8)
    k=torch.randn(2,3,5,8)
    v=torch.randn(2,3,5,8)
    reference=torch.nn.functional.scaled_dot_product_attention(q,k,v)
    actual=optimized_attention(q,k,v,3,skip_reshape=True,skip_output_reshape=True)
    torch.testing.assert_close(actual,reference)
    identity=torch.eye(2).reshape(1,1,1,1,2,2).expand(1,4,1,4,2,2)
    x=torch.randn(1,4,3,8)
    torch.testing.assert_close(apply_rope1(x,identity),x)
