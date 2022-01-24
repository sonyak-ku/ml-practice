import numpy as np
import torch

# tensor = torch.rand(size=(3, 2))
# print(tensor)
# b = tensor.view(6)
# print(b)
# c = tensor.t().reshape(6)
# print(c)

a = torch.zeros(3, 2)
b = a.reshape(6)
c = a.t().reshape(6)
# d = a.t().view(6)
a.fill_(1)

a = torch.rand(5)
# print(a.shape)
# print(a.unsqueeze(1).shape)
# print(a.shape)
# print(a)
# print(d)

a = torch.rand(5, 2, 3)
b = torch.rand(3)

print(a[0].mm(torch.unsqueeze(b, 1 )))

c = torch.rand(3)
d = torch.rand(3, 1)
# print(d.mm(c.unsqueeze(0)))
# print(c.unsqueeze(1))

p = torch.randint(4, (10, 5))
print(p)