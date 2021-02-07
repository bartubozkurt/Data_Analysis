import numpy as np

sayilar = np.array([0,5,10,15,20,25,30])

print(sayilar[::-1])  # sayilar dizisini tersten diz
print(sayilar[5])
print(sayilar[0:3])
print('----------------------')
sayilar2 = np.array([[0,5,10],[15,20,25]])
print(sayilar2[0])  # [ 0  5 10]
print(sayilar2[1])  # [15 20 25]
print(sayilar2[1,2]) # 25
print(sayilar2[:,2]) # tüm satırlardan 2 elemanı ver [10 25]
print(sayilar2[:,0]) # tüm satırlardan 0 elemanı ver  [ 0 15]
print(sayilar2[:,0:2])
# 0 ncı sütündan 2 ci stüna kadar olanları ver fakat 2 dahil değil
""" [[ 0  5]
    [15 20]] """
print(sayilar2[-1,:])   # [15 20 25] son satırdaki data
print(sayilar2[:,-1])  # [10 25] en sütun daki tüm satırları ver
