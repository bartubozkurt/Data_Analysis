import numpy as np

a = np.floor(10*np.random.random((2,3)))
""" [[9. 7. 8.]
    [4. 2. 1.]] """

b = np.floor(10*np.random.random((2,3)))
""" [[1. 3. 5.]
    [6. 0. 7.]] """

print(a)

print('-----------')

print(b)

print('-----------')

c = np.vstack((a,b)) 
""" [[9. 7. 8.] 
     [4. 2. 1.]
     [1. 3. 5.]
    [6. 0. 7.]]
 """
print(c)

print('-----------')

d = np.hstack((a,b))
""" [[9. 5. 8. 1. 8. 1.]
    [2. 3. 5. 1. 0. 5.]] """
print(d)
