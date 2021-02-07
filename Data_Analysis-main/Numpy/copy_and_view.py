import numpy as np

a = np.arange(10)
print(a)

b = a
print(b)
print(a[2])
print(b[2])

b[0] = 100 
print(a)
print(b)

c = a.copy()

print('----------------')

print(c)
c[0] = 1000

print('----------------')

print(a)
print(c)

print('----------------')
print('*')
d = a.view() 
print(a)
print(d)
d[0] = 250
print(a)
print(d)
d.shape = 2,5
print('----------------')
a[0] = 125
print(a)
print(d)


