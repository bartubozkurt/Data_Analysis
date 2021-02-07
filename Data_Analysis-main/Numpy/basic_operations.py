import numpy as np

a = np.array([20,30,40,50])     # [20 30 40 50]
b = np.arange(4)        # [0 1 2 3]
print(a)
print(b)

c = a-b
print(c)

""" [20 30 40 50]
    [0 1 2 3]
    [20 29 38 47]
    """

d = b**2    # [0 1 4 9]
print(d)

e = 10 * np.sin(a)      # [ 9.12945251 -9.88031624  7.4511316  -2.62374854]
print(e)

print(e < 7)        # [False  True False  True]
print(a*b)     # [  0  30  80 150]

print(a@b)     # matris çarpımı sonucu : 260
print(a.dot(b)) # matris çarpımı sonucu : 260

f = np.ones((2,4)) 

""" [[1. 1. 1. 1.]
 [1. 1. 1. 1.]] """

g = np.zeros((2,4))

""" [[0. 0. 0. 0.]
 [0. 0. 0. 0.]] """

h = np.random.random((2,4))

""" [[0.24448762 0.30569748 0.38721877 0.42359117]
 [0.74705078 0.64296611 0.87855028 0.44236936]] """

i = np.sum(b)     # 6

j  = np.min(c)    # 20

k = np.max(h)     # 0.8785502826111841

l =np.sqrt(b)     # [0.         1.         1.41421356 1.73205081]

print(f)
print('----------------------')
print(g)
print('----------------------')
print(h)
print('----------------------')
print(i)
print('----------------------')
print(j)
print('----------------------')
print(k)
print('----------------------')
print(l)