import numpy as np

###########################################

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

x[1::2] = (-1)
print(x)

###########################################

x = np.arange(10)
x = np.resize(x,10).reshape(2,5)
print(x)

############################################

x = np.array([1,2,3])
print(np.append(np.repeat(x,3),np.tile(x,3)))


############################################

x = np.array([1,2,3,2,3,4,3,4,5,6])
y = np.array([7,2,10,2,7,4,9,4,9,8])
print(np.intersect1d(x, y))

############################################

x = np.array([1,2,3,2,3,4,3,4,5,6])
y = np.array([7,2,10,2,7,4,9,4,9,8])

print(np.where(x == y)[0])

############################################

print(np.random.uniform(5,10,(5,3)))

############################################

np.random.seed(100)
x = np.random.random([3,3])/1e3
np.set_printoptions(precision = 6, suppress = True)
print(x)

############################################

np.random.seed(100)
x = np.random.random([3,3])/1e3
np.set_printoptions(suppress = True)
print(x)

############################################

x = np.arange(9).reshape(3,3)
x[:,[0, 1]] = x[:,[1, 0]]
print(x)

############################################

x = np.arange(9).reshape(3,3)
x[[0,2]] = x[[2,0]]
print(x)
