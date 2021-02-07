import numpy as np

havaDurumu = [[12,21,31],[6,17,18],[11,12,13]]
print(havaDurumu)

print('-----------------------------------------')

a = np.arange(15).reshape(3,5)
print(a)
print(type(a))
print("Dimension Count : " + str(a.ndim)) # Boyut

print('-----------------------------------------')

b = np.arange(10)
print(b.shape)
print(b)
print(type(b)) 
print("Dimension Count : " + str(b.ndim)) #Boyut