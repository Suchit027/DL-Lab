import torch


a = torch.tensor(5)
print(a)

b = torch.tensor([1, 1])
# note
print(b.ndim)


a = torch.rand(size=(3, 4))
print(a, a.dtype)

# note
print(a.shape)

# note
a = torch.zeros(size=(3, 4))
print(a)

# note
a = torch.ones(size=(3, 4))
print(a)

# note
a = torch.arange(1, 10, 2)
print(a)

# note
a = torch.zeros_like(a)
print(a)