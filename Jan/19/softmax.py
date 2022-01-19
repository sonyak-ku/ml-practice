import numpy as np

a = [1, 0, -1]

# print(np.max(a))
d = np.exp(a)
# print(d)
# print(a - np.max(a))
d = np.exp(a - np.max(a, axis=-1, keepdims=True))
n = np.sum(d, axis=-1, keepdims=True)

print(d / n)