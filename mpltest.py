import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
https://www.kaggle.com/datasets
    • Övning: visualisera data (linjediagram, histogram).
Det betyder att du ska:    1. Läsa in ett dataset (CSV)    2. Skapa ett linjediagram    3. Skapa ett histogram
    4. Förstå vad graferna visar
    production_share_pct, mine_production_tonnes, price_usd_per_tonne 
"""


df = pd.read_csv("critical_minerals_supply_master.csv")
lands = ["China", "Australia", "Brazil", "Canada", "France", "Peru", 'Tajikistan', 'USA', 'Rwanda']
plt.figure(figsize=(12,6))

df["year"] = df["year"].astype(int)
"""
for land in lands:
    group = (
        df[df["country"] == land]
        .groupby("year")["mine_production_tonnes"]
        .mean()
    )
    plt.plot(group.index, group.values)

plt.xlabel("Year")
plt.ylabel("mine_production_tonnes")
plt.title("Average mine production ")
"""

plt.figure(figsize=(12,6))

plt.hist(df["mine_production_tonnes"], bins=30)
plt.title("Distribution of price per tonne")
plt.xlabel("USD per tonne")
plt.ylabel("Frequency")
plt.show()

