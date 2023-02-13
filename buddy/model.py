"""
params = {
  "layers": 28,
  "d_model": 4096,
  "n_heads": 16,
  "n_vocab": 50400,
  "norm": "layernorm",
  "pe": "rotary",
  "pe_rotary_dims": 64,

  "seq": 2048,
  "cores_per_replica": 8,
  "per_replica_batch": 1,
}

Model Details:
n_parameters	6,053,381,344
n_layers	    28*
d_model	        4,096
d_ff	        16,384
n_heads     	16
d_head      	256
n_ctx           2,048

# maybe it should be 50304 for n_vocab?
# GPT-2 vocab_size of 50257, padded up to nearest multiple of 64 for efficiency
# from nanoGPT
n_vocab         50,257

"""
import math

import torch 
import torch.nn as nn
from torch.nn import functional as F

def new_gelu(x):
    """
    Implementation of the GELU activation function currently in Google BERT repo (identical to OpenAI GPT).
    Reference: Gaussian Error Linear Units (GELU) paper: https://arxiv.org/abs/1606.08415
    """
    return 0.5 * x * (1.0 + torch.tanh(math.sqrt(2.0 / math.pi) * (x + 0.044715 * torch.pow(x, 3.0))))

class LayerNorm(nn.Module):
  """ Layer norm with optional bias """
  def __init__(self,ndim, bias):
    super().__init__()
    self.weight = nn.Parameter(torch.ones(ndim))
    self.bias = nn.Parameter(torch.zeros(ndim)) if bias else None
  
  def forward(self, input):
    return F.layer_norm(input, self.weight.shape, self.weight, self.bias, 1e-5)

class CausalSelfAttention(nn.Module):

  def __init__(self, config):
    super().__init__()









if __name__ == "__main__":
    print("Buddy")