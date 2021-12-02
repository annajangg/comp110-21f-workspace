import numpy as np

# https://numpy.org/doc/stable/user/absolute_beginners.html
# https://numpy.org/doc/stable/reference/arrays.ndarray.html#array-methods

x = np.arange(1, 5)
print(x)
print(x * 2)
print(x % 2 == 1)
print(x[x % 2 == 1])
print(x.std())
