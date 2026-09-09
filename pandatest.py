"""
assignment: load csv-file in pandas. look at the structure, count statistics (mean, median,std)
filter different species and values and make a few simple vizualisations.
EDA (Exploratory Data Analysis).
1 explore the data structure --- df.info() → datatypes, null‑values
df.describe() → statistics (mean, std, min, max),   df.shape → numer of rows/columns
df["species"].value_counts() → 50 of every species (setosa, versicolor, virginica)
2   count statistics per column, median, mean, corr.
3   Filter data ---  All setosa:,  Petal length > 5:, combined conditions:
4   Groupbased statistics, count statistics per species: df.groupby("species").agg(["mean","std","min","max"])
5   Vizualisations (optional but recommended) Use matplotlib or seaborn
"""
import matplotlib.pyplot as plt
import pandas as pd
# noinspection PyArgumentList
df =  pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")

#print(df.select_dtypes(include="number").corr())  # to sort away STR columns by CORR
#print(df[(df["species"] == "setosa") & (df["petal_length"] > 1.6)]) #combines conditions by filtering
#print (df.groupby("species").agg(["std"]))

df.info()
#df1 = df.groupby(["species"]).mean()
#print (df1)
#bars = plt.bars(df1.index, df1.sepal_length)
# noinspection PyArgumentList
df.boxplot(column="sepal_length",by="species")

plt.xlabel("species")
plt.ylabel("sepal length")
plt.show()