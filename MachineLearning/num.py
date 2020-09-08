import numpy as np

a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
b = np.eye((10))
c = np.zeros((10, 10))
d = np.ones((10, 10))

print(a)
print(a.max())
print(a.min())
print(a.sum())
print(a.mean())
print(a.std())
print(b)
print(c)
print(d)


