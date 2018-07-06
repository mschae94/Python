import pandas as pd
import numpy as np

data = [[1.4, np.nan],
           [7.1, -4.5],
        [np.nan, np.nan],
        [0.75, -1.3]]
df = pd.DataFrame(data, columns=["one", "two"], index=["a", "b", "c", "d"])
print(df)
test = df.sum(axis =0)
print(test)
test = df.sum(axis = 1)
print(test)

test =df["one"].sum()
print(test)
test =df.loc["b"].sum()
print(test)
test = df.mean(axis=1,skipna=False)
print(test)

one_mean = df.mean(axis =0)["one"]
two_min =df.min(axis=0)["two"]
df["one"] = df["one"].fillna(value=one_mean)
print(df)
df["two"] = df["two"].fillna(value= two_min)
print(df)

df2 = pd.DataFrame(np.random.rand(6, 4),
                   columns=["A", "B", "C", "D"],
                   index=pd.date_range("20160701", periods=6))
print(df2)
# test =df2["A"].corr(df2["B"])
# print(test)
# test = df2["B"].cov(df2["C"])
# print(test)
dates = df2.index
random_dates = np.random.permutation(dates)
df2 = df2.reindex(index=random_dates, columns=["D", "B", "C", "A"])
print(df2)
test = df2.sort_index(axis =0)
print(test)
test = df2.sort_index(axis =1)
print(test)
test = df2.sort_index(axis =0 , ascending = False)
print(test)

#값기준정렬
test = df2.sort_values(by="D")
print(test)
test = df2.sort_values(by="B")

df2["E"] = np.random.randint(0, 6, size=6)
df2["F"] = ["alpha", "beta", "gamma", "gamma", "alpha", "gamma"]

print(df2)
test = df2.sort_values(by=["E", "F"])
print(test)

test =df2["F"].unique()

print(test)
test = df2["F"].value_counts()
print(test)
test = df2["F"].isin(["alpha","beta"])
print(test)

test = df2.loc[df2["F"].isin(["alpha" ,"beta"]),:]
print(test)

df3 = pd.DataFrame(np.random.rand(4, 3), columns=["b", "d", "e"],
                   index=["Seoul", "Incheon", "Busan", "Daegu"])

print(df3)

func = lambda x: x.max()- x.min()
test =df3.apply(func , axis = 0)
print(test)
test =df3.apply(func , axis = 1)
print(test)
