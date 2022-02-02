import torch

a = torch.randn((2,2), requires_grad = True)
print(a)
w1 = torch.randn((2,2), requires_grad = True)
w2 = torch.randn((2,2), requires_grad = True)
w3 = torch.randn((2,2), requires_grad = True)
w4 = torch.randn((2,2), requires_grad = True)


b = w1*a
c = w2*a

d = w3*b + w4*c

L = 10 - d

L.backward(torch.ones(L.size()))

### 원래는 backward 는 스칼라형태의 input 에서만 가능하지만, 벡터형태의 input 에서도 이를 가능하게끔 하는 몇가지 조작이 있다.
# 1.L.backward(torch.ones(L.size()))
# 2.L = torch.sum(10-d)