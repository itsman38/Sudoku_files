import numpy as np

a = np.array([1, 2, 3], dtype="int8")
b = np.array([[1, 2, 3, 4, 5, 6],
              [7, 8, 9, 10, 11, 12]])  # have same length for all rows

print(a)
print(a.ndim)
print(a.shape)
print(a.dtype)

print("\n")
print(b)
print(b.ndim)  # no of dimension of array
print(b.shape)  # matrix dimensions
print(b.dtype)
print(a.itemsize)  # no of bytes per item (int 8 = 1 byte)
print(a.size)  # no of elements
print(a.nbytes)  # total no of bytes

print("\n")
print(b[0, 0])
print(b[1, 5])
print(b[0, -1])
print(b[0, :])  # for row
print(b[:, 4])  # for col
print(b[0, 1:6:2])  # start-index: end-index: steps

print("\n")
c = np.array([[[1, 2],  # 3d array
               [3, 4]],

              [[5, 6],
               [7, 8]]])

print(c[0, 1, 0])  # work outside in (dimension, row, element)

print("\n")
zero = np.zeros((1, 2))
print(zero)

print("\n")
one = np.ones((2, 2, 3))
print(one)

print("\n")
other = np.full((2, 4), 21)     # size, value
print(other)

print("\n")
decimal = np.random.rand(2, 3)
print(decimal)

print("\n")
int1 = np.random.randint(10, size=(2, 4))
print(int1)

print("\n")
int2 = np.random.randint(-5, 5, size=(3, 3))   # min, max(exclusive), size

print("\n")
print(np.identity(3))

print("\n")
arr = np.array([[1, 2, 3]])
r1 = arr.repeat(3, axis=0)  # axis 0 = row
r2 = arr.repeat(2, axis=1)
print(r1)
print(r2)

print("\n")
print("test matrix")

new = np.ones((5, 5))
rep = np.zeros((3, 3))
rep[1, 1] = 9
new[1:4, 1:4] = rep
print(new)

# to copy arrays don't assign but use copy
print("\n")
a = np.array([1, 2, 3])
b = a
b[0] = 100  # assigns the value of a[0] to 100 as well
print(a)

# instead
a = np.array([1, 2, 3])
b = a.copy()
b[0] = 100
print(a)
print(b)

print("\n")


                                                    # MATH


a = np.array([1, 2, 3, 4])

print(a)
print(a + 2)
print(a - 2)
print(a * 2)
print(a / 2)
print(a ** 2)
print(np.sin(a))
print(np.cos(a))


                                                # LINEAR ALGEBRA


print("\n")
a = np.ones((2, 3))
b = np.full((3, 2), 5)
c = np.matmul(a, b)  # if not same shape then a*b doesn't work
print(c)

print("\n")
d = np.identity(3)
print(np.linalg.det(d))


                                                    # STATISTICS


print("\n")
a = np.array([1, 2, 3])
b = np.array([[4, 5, 6],
             [7, 8, 9]])

print(np.max(a))
print(np.max(b))
print(np.max(b, axis=0))
print(np.max(b, axis=1))
print(np.sum(b))            # sum of all elements
print(np.sum(b, axis=0))    # sum of elements of col
print(np.sum(b, axis=1))    # sum of elements of row


                                                    # RESHAPING


print("\n")
old = np.array([[1, 2, 3, 4],
               [5, 6, 7, 8]])

new = old.reshape((4, 2))
print(new)
print("\n")

new = old.reshape((1, 8))
print(new)
print("\n")

new = old.reshape((2, 2, 2))  # must have equal number of elements as old
print(new)
print("\n")


                                                    # STACKING


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a, b)
print("\n")
c = np.vstack((a, b))     # cannot stack if shape mismatch
print(c)
print("\n")

c = np.vstack((a, b, b, a))
print(c)
print("\n")

a = np.zeros((2, 2))
b = np.ones((2, 3))

c = np.hstack((a, b))
print(c)

# LOADING DATA FROM FILE

print("\n")
data = np.genfromtxt("test_files/numbers.txt", delimiter=",")   # all rows must have same no of col
data = data.astype("int16")
print(data)


                                        # BOOLEAN MASKING AND ADVANCED INDEXING


print("\n")
a = np.array([1, 2, 3, 4, 5])
print(a[[0, 1, 3]])     # can pass lists for index in numpy

print("\n")
print(data > 10)        # prints bool of values > 10
print("\n")
print((data > 10) & (data <= 15))
print("\n")
print(~((data > 10) & (data <= 15)))    # ~ = not

print("\n")
print(data[data > 10])  # prints all values > 10

print("\n")
print(np.any(data > 10, axis=0))    # checks if any col has at least one value > 10
print(np.any(data > 10, axis=1))    # checks if any row has at least one value > 10

print("\n")
print(np.all(data > 10, axis=0))    # checks if any col has all values > 10
print(np.all(data > 10, axis=1))    # checks if any row has all values > 10


# test 2

a = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20],
             [21, 22, 23, 24, 25],
             [26, 27, 28, 29, 30]])

print(a)
print(a[2:4, :2])
print(a[[0, 1, 2, 3], [1, 2, 3, 4]])
print(a[[0, 4, 5], 3:])

