import numpy as np

t1 = np.array([[1, 0, 1], [0, 1, 0], [1, 1, 0]])

t2 = np.linalg.inv(t1)

print(t2)

p1 = np.array([[1, 0, 1], [0, 1, 0]])

p2 = np.linalg.pinv(p1)

print(p2)