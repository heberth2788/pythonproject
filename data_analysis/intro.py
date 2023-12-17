# Pandas library

from pandas import *
import pandas as pd

# Load data from .csv file
data: DataFrame = pd.read_csv("base.csv")
head: DataFrame = data.head()
print("\n", head)

sexCounts = data["Sexo"].value_counts()
print("\nCounts", sexCounts)

sexPercent = data["Sexo"].value_counts(normalize = True)
print("\nPercent", sexPercent)

distribution = pd.DataFrame(
    {"counts" : sexCounts, "porcentaje" : sexPercent}
)
sexRename = {0 : "Male", 1 : "Female"}
distribution.rename(index = sexRename, inplace = True)
print("\n", distribution)

# Matplot


