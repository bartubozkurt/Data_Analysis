import numpy as np

a = np.floor(10 * np.random.random((3,4)))
print(a)
print(a.shape) # 3 e 4 dizi
print(a.ravel()) # diziyi listeye dönüştürme (gecici olarak)
a = a.ravel() # diziyi liste dönüştürme 
print(a)
print(a.shape) # 12 elemanlı düz bir dizi imiş
print(a.reshape(2,6))

""" [[5. 8. 5. 0. 7. 6.]
    [1. 9. 5. 7. 9. 9.]]
 """

print('-------------------------------')

a = a.reshape(2,6)
""""[[5. 1.]
    [8. 9.]
    [5. 5.]
    [0. 7.]
    [7. 9.]
    [6. 9.]] """
print(a)
print(a.T)
