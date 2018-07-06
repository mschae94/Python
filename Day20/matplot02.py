#%matplotlib nbagg
import matplotlib
import  matplotlib.pyplot as plt
import pandas as pd
import numpy as np


fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)

ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

plt.plot(np.random.randn(50).cumsum())

ax1.hist(np.random.randn(100), bins=20)
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))

fig, axes = plt.subplots(2, 3)

plt.plot(np.random.randn(30), color="g", marker='o', linestyle="--")

plt.plot(np.random.randn(30), "k.-")

fig, axes = plt.subplots(2, 1)
data = pd.Series(np.random.rand(16), index=list('abcdefghijklmnop'))
data.plot(kind="bar", ax=axes[0], color='k', alpha=0.7)
data.plot(kind="barh", ax=axes[1], color='g', alpha=0.3)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(1000).cumsum())

ticks = ax.set_xticks([0, 250, 500, 750, 1000])

labels = ax.set_xticklabels(["one", "two", "three", "four", "five"],
                            rotation=30, fontsize="small")

ax.set_title("Random walk plot")
ax.set_xlabel("Stages")
ax.set_ylabel("Values")

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


ax.plot(np.random.randn(1000).cumsum(), 'k', label="one")
ax.plot(np.random.randn(1000).cumsum(), "b--", label="two")
ax.plot(np.random.randn(1000).cumsum(), "r.", label="three")

ax.legend(loc="best")

ax.set_xlim([100, 900])
ax.set_ylim([-100, 100])