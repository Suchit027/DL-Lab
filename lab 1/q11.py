import torch

a = torch.rand(size=(1, 1, 1, 10))
a = a.squeeze()
print(a)

# note manual seed
torch.manual_seed(7)
a = torch.rand(size=(1, 1, 1, 10))
a = a.squeeze()
print(a)