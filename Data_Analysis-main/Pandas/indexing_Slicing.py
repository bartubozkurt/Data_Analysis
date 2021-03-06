import pandas as pd

grades = pd.read_csv("grades.csv")
grades.columns = ["Name","Surname","SSN","Test1","Test2","Test3","Test4","Final","Sonuc"]
print(grades)

print(grades.loc[:,"Name"]) # Name kolonunu verir
print(grades.loc[:5,"Name"])
print(grades.loc[:5,"Name" : "Test4"]) # ilk 5 kişinin  isimlerinden Test4 lerine kadar olan bilgilerini getir
"""
       Name           Surname                   SSN  Test1  Test2  Test3  Test4
0  Alfalfa        "Aloysius"         "123-45-6789"   40.0   90.0  100.0   83.0
1   Alfred      "University"         "123-12-1234"   41.0   97.0   96.0   97.0
2    Gerty          "Gramma"         "567-89-0123"   41.0   80.0   60.0   40.0
3  Android        "Electric"         "087-65-4321"   42.0   23.0   36.0   45.0
4  Bumpkin            "Fred"         "456-78-9012"   43.0   78.0   88.0   77.0
5   Rubble           "Betty"         "234-56-7890"   44.0   90.0   80.0   90.0 
"""
print(grades.loc[:5,["Name" , "Surname" , "Final"]])
"""
       Name     Final
0  Alfalfa      49.0
1   Alfred      48.0
2    Gerty      44.0
3  Android      47.0
4  Bumpkin      45.0
5   Rubble      46.0 
"""

