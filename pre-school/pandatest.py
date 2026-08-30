"""
Ladda CSV‑filen i Pandas, titta på strukturen, räkna statistik (mean, median, std),
filtrera fram olika species och värden, och gör några enkla visualiseringar.
Det här blir din första riktiga EDA (Exploratory Data Analysis).
1   Utforska datans struktur --- df.info() → datatyper, null‑värden
df.describe() → statistik (mean, std, min, max),   df.shape → antal rader/kolumner
df["species"].value_counts() → 50 av varje art (setosa, versicolor, virginica)
2   Räkna statistik per kolumn, median, mean, corr,
3   Filtrera data ---  Alla setosa:,  Petal length > 5:, Kombinerade villkor:
4   Gruppbaserad statistik, Räkna statistik per art: df.groupby("species").agg(["mean","std","min","max"])
5   Visualiseringar (valfritt men rekommenderat)   Du kan använda matplotlib eller seaborn.
"""
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")

#print(df.select_dtypes(include="number").corr())  # för att sortera bort STR kolumner vid CORR
#print(df[(df["species"] == "setosa") & (df["petal_length"] > 1.6)]) #kombinerar villkor vid filtrering
#print (df.groupby("species").agg(["std"]))

df.info()
#df1 = df.groupby(["species"]).mean()
#print (df1)
#bars = plt.bars(df1.index, df1.sepal_length)

df.boxplot(column="sepal_length",by="species")

plt.xlabel("species")
plt.ylabel("sepal length")
plt.show()