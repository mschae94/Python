import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#바 플롯
s = pd.Series(np.random.rand(10).cumsum(),
              index = np.arange(0,100,10))
print(s)
s.plot()

df2 = pd.DataFrame(np.random.rand(6,4),
                   index =["one" , "two" ,"three" ,"four","five","six"],
                   columns=pd.Index(["A" ,"B" , "C" ,"D"],name="Genus"))
df2.plot(kind="bar")
df2.plot(kind="barh", stacked= True)

s2 = pd.Series(np.random.rand(16) , index=list("abcdefghijklmnop"))
s2.plot(kind="bar")
s2.plot(kind="barh")








