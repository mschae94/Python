import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

battle = pd.read_csv("09_python_0930_pbu/Day20/game-of-thrones/battles.csv",sep=",")
deaths = pd.read_csv("09_python_0930_pbu/Day20/game-of-thrones/character-deaths.csv",sep=",")

battle.shape
battle.columns
deaths.shape
deaths.columns


book_nums_to_death_count = deaths["Book of Death"].value_counts().sort_index()
ax1 =book_nums_to_death_count.plot(color="k", marker="o", linestyle="--")
ax1.set_xticks(np.arange(1,6))
ax1.set_xlim([0,6])
ax1.set_ylim([0,120])



battles = battle.set_index(["name"])
large_battles_mask = battles["attacker_size"] + battles["defender_size"] > 10000
large_battles = battles.loc[large_battles_mask, ["attacker_size", "defender_size"]]
ax2 = large_battles.plot(kind="barh", stacked=True, fontsize=8)



large_battles["attacker_pcts"] = \
    large_battles["attacker_size"] / (large_battles["attacker_size"] + large_battles["defender_size"])
large_battles["defender_pcts"] = \
    large_battles["defender_size"] / (large_battles["attacker_size"] + large_battles["defender_size"])
ax3 = large_battles[["attacker_pcts", "defender_pcts"]].plot(kind="barh", stacked=True, fontsize=8)


col_names = battles.columns[4:12]
house_names = battles[col_names].fillna("None").values
house_names = np.unique(house_names)
house_names = house_names[house_names != "None"]
houses_to_battle_counts = pd.Series(0, index=house_names)
for col in col_names:
    houses_to_battle_counts = \
        houses_to_battle_counts.add(battles[col].value_counts(), fill_value=0)
ax4 = houses_to_battle_counts.hist(bins=10)



