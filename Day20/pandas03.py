import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(6,4))
print(df)
df.columns = ["a" , "b",  "c", "d"]
df.index = pd.date_range("20171003", periods=6)
print(df.index)
print(df)
df["F"] = [1.0 , np.nan , 3.5 , 6.1 , np.nan , 7.0]
print(df)
print(df.isnull())
test = df.loc[df.isnull()["F"],:]
print(test)
test = pd.to_datetime(("20171011"))
print(test)
test = df.drop(pd.to_datetime(("20171003")))
print(test)
test = df.drop([pd.to_datetime("20171004"), pd.to_datetime("20171007")])
print(test)
test = df.drop("F",  axis=1)
print(test)
test = df.drop(["b" , "F"],  axis=1)
print(test)








