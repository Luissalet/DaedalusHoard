import torch
import torch.nn.functional as F
from daedalus.geometry.ultra_model import PackedAttention,rotary_grid,rotate

def test_checkpoint_head_packing_against_explicit_attention():
    torch.manual_seed(17)
    attention=PackedAttention(12,3).eval()
    x=torch.randn(2,5,12)
    # This checkpoint packs concatenated projections head-first, rather than
    # splitting each projection into heads separately.
    packed=torch.cat([attention.to_q(x),attention.to_k(x),attention.to_v(x)],-1).reshape(2,5,3,12)
    q,k,v=packed.split(4,dim=-1)
    q=attention.q_norm(q).transpose(1,2);k=attention.k_norm(k).transpose(1,2);v=v.transpose(1,2)
    probabilities=(q@k.transpose(-1,-2)/2).softmax(-1)
    expected=attention.out_proj((probabilities@v).transpose(1,2).reshape(2,5,12))
    torch.testing.assert_close(attention(x),expected,atol=2e-6,rtol=2e-6)

def test_rotary_grid_is_identity_at_origin_and_preserves_norm():
    x=torch.randn(2,3,5,128)
    origin=rotary_grid(torch.zeros(2,5,3,dtype=torch.int64))
    torch.testing.assert_close(rotate(x,origin),x)
    shifted=rotary_grid(torch.randint(0,128,(2,5,3)))
    torch.testing.assert_close(rotate(x,shifted).norm(dim=-1),x.norm(dim=-1))
    assert rotate(x.bfloat16(),shifted).dtype==torch.bfloat16
