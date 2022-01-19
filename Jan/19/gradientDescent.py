import numpy as np

X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(X, np.array([1, 2])) + 3 # 3은 y 인터셉트

print(X)
print(y)

beta = [10.1, 15.1, -6.5] #[1, 2, 3] 이 정답
x_ = np.array([np.append(x, [1]) for x in X]) # 인터셉트항 추가
print(x_ @ beta)


for t in range(5000):
    error = y - x_ @ beta
    # error = error / np.linalg.norm(error)
    grad = - np.transpose(x_) @error
    beta = beta - 0.01 * grad

print(beta)