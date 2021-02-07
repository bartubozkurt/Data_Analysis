import pandas as pd
import numpy as np

data = np.array(["Bartu","Bozkurt","Osman"])
# s = pd.Series(data)
s = pd.Series(data ,index = [1,2,3])
print(s)
""" 
    0      Bartu
    1    Bozkurt
    2      Osman
    dtype: object
"""
""" 
    1      Bartu
    2    Bozkurt
    3      Osman
    dtype: object 
"""
print('-----------------------------------')

data2 = {"Matematik" : 10, "Fizik": 20,"Beden Eğitimi": 100}
#s2 = pd.Series(data2)
s2 = pd.Series(data2, index = ["Fizik","Matematik","Beden Eğitimi"])
print(s2)
""" 
    Matematik         10
    Fizik             20
    Beden Eğitimi    100
    dtype: int64 
"""
""" 
    Fizik             20
    Matematik         10
    Beden Eğitimi    100
    dtype: int64 
"""

print('-----------------------------------')

s3 = pd.Series(5, index = [1,2,3])
print(s3)
"""
    1    5
    2    5
    3    5
    dtype: int64
 """

