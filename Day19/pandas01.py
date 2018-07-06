import numpy as np
import pandas as pd

obj = pd.Series([4,5,-2,1])
print(obj)
print(obj.values)
print(obj.index)
obj2 = pd.Series([4,5,-2,1], index=["d","c" ,"a","k"])
print(obj2)
sdata = {"kim":35000,"ha":70020,"park":5000,"joe":45000}
print(sdata)
obj3 = pd.Series(sdata)
print(obj3)
obj3.name = "Salary"
obj3.index.name = "Names"
print(obj3)
obj3.index = ["a" , "b" ,"c","d"]
print(obj3)
data = {"names" :["kim","kim" ,"kim" , "park","ha"],
        "year" :[2014,2015,2010,2016,2010],
        "points":[1.5,1.7,1.3,1.2,2.0]}
df = pd.DataFrame(data)
print(df)
print(df.index)
print(df.columns)
df.index.name = "Num"
df.columns.name = "Info"
print(df)
df2 = pd.DataFrame(data , columns= ["year" , "names" ,"points" ,"penalty"],
                   index = ["one","two","three","four","five"])
print(df2)




