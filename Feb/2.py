import torch

a = torch.randn(1, requires_grad = True)
print(a)
w1 = torch.randn(1, requires_grad = True)
w2 = torch.randn(1, requires_grad = True)
w3 = torch.randn(1, requires_grad = True)
w4 = torch.randn(1, requires_grad = True)


b = w1*a
c = w2*a

d = w3*b + w4*c

L = (10 - d)

L.backward()