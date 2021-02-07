import pandas as pd

grades = pd.read_csv("grades.csv")
grades.columns = ["Name","Surname","SSN","Test1","Test2","Test3","Tes4","Final","Sonuc"]
print(grades)
print(type(grades)) # <class 'pandas.core.frame.DataFrame'>
print(grades.head()) # ilk 5 kayıt
print('------------------------------------------------------------------------------------------------------------')
print(grades.tail()) # son 5 kayıt
"""
  Last name      "First name"                 "SSN"         "Test1"   "Test2"   "Test3"   "Test4"   "Final"  "Grade"
0   Alfalfa        "Aloysius"         "123-45-6789"            40.0      90.0     100.0      83.0      49.0     "D-"
1    Alfred      "University"         "123-12-1234"            41.0      97.0      96.0      97.0      48.0     "D+"
2     Gerty          "Gramma"         "567-89-0123"            41.0      80.0      60.0      40.0      44.0      "C"
3   Android        "Electric"         "087-65-4321"            42.0      23.0      36.0      45.0      47.0     "B-"
4   Bumpkin            "Fred"         "456-78-9012"            43.0      78.0      88.0      77.0      45.0     "A-"
-------------------------------------------------------------------------------------------------------------------
      Last name  "First name"                  "SSN"         "Test1"   "Test2"   "Test3"   "Test4"   "Final"  "Grade"
11      Dandy         "Jim"          "087-75-4321"            47.0       1.0      23.0      36.0      45.0     "C+"
12   Elephant         "Ima"          "456-71-9012"            45.0       1.0      78.0      88.0      77.0     "B-"
13   Franklin       "Benny"          "234-56-2890"            50.0       1.0      90.0      80.0      90.0     "B-"
14     George         "Boy"          "345-67-3901"            40.0       1.0      11.0      -1.0       4.0      "B"
15  Heffalump      "Harvey"          "632-79-9439"            30.0       1.0      20.0      30.0      40.0      "C"
"""
print('------------------------------------------------------------------------------------------------------------')

print(grades["Final"]) # Final notlarını getir
print(grades.iloc[2])   # 2. index in bilgilerini getir
print(grades[0:10])  # 0 9 arasında 10 kişiyi getir