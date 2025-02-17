import torch

a = torch.rand(size=(3, 4))
print(a)

# note
a = torch.permute(a, dims=(1, 0))
print(a)