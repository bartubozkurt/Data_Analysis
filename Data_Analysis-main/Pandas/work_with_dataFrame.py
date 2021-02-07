import pandas as pd

df = pd.DataFrame()
print(df)
""" 
    Empty DataFrame
    Columns: []
    Index: [] 
"""
print('-------------------------------')
data = [10,20,30,40,50]
df = pd.DataFrame(data)
print(df)
"""     
        0
    0  10
    1  20
    2  30
    3  40
    4  50
 """
print('-------------------------------')
data2 = [["Bartu", 21,"İzmir"],["Osman",18 ,"İstanbul"],["Ali",32,"Ankara"]]
# df2 = pd.DataFrame(data2)
df2 = pd.DataFrame(data2, columns=["İsim","Yaş","Şehir"],index = [1,2,3])
print(df2)
"""  
        0      1         2
    0  Bartu  21     İzmir
    1  Osman  18  İstanbul
    2    Ali  32    Ankara
"""
"""     
        İsim  Yaş     Şehir
    0  Bartu   21     İzmir
    1  Osman   18  İstanbul
    2    Ali   32    Ankara 
"""
print('-------------------------------')
data3 = {"İsim": ["Bartu","Osman","Bozkurt"],
        "Yaş": [21,18,32],
        "Şehir": ["İzmir","İstanbul","Ankara"]}

df3 = pd.DataFrame(data3, columns=["İsim","Yaş","Şehir"],index = [1,2,3])
print(df3)
"""
          İsim  Yaş     Şehir
    1    Bartu   21     İzmir
    2    Osman   18  İstanbul
    3  Bozkurt   32    Ankara
"""
print(df3["İsim"])
"""

    1      Bartu
    2      Osman
    3    Bozkurt
"""
# Şehir kolonunu uçurur
# del df3["Şehir"] ya da df3.pop("Şehir")
# print(df3) 
print('-------------------------------')

print(df3.loc[2]) # index göre sıralanmış dataları loc eder
"""
    İsim        Osman
    Yaş            18
    Şehir    İstanbul
    Name: 2, dtype: object 
"""
print(df3.iloc[1]) # index yerine verinin sırası önemli 0 dan başlıyor....
"""
    İsim        Osman
    Yaş            18
    Şehir    İstanbul
    Name: 2, dtype: object 
"""
print('-------------------------------')
df4 = df3.append(df2) # data genişledi
print(df4)
"""
          İsim  Yaş     Şehir
    1    Bartu   21     İzmir
    2    Osman   18  İstanbul
    3  Bozkurt   32    Ankara
    1    Bartu   21     İzmir
    2    Osman   18  İstanbul
    3      Ali   32    Ankara
 """
 