import torch

a = torch.rand(size=(3, 4))
print(a)

b = a.reshape(shape=(4, 3))
print(b)

b = a.view(size=(4, 3))
print(b)

a = torch.tensor([1, 2])
b = torch.tensor([2, 3])
c = torch.tensor([3, 4])
d = torch.stack((a, b, c), dim= 1)
print(d)
d = torch.stack((a, b, c), dim= 0)
print(d)


a = torch.rand(size=(1, 2, 1, 3))
print(a)
a = torch.squeeze(a)
print(a)

# note dim
print(a.shape)
a = torch.unsqueeze(a, dim= 2)
print(a, a.shape)