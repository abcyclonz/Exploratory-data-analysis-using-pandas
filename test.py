import pandas as pd
df = pd.read_csv("fileName.csv")
df.head(10)
df.shape
df[df["Event1"]=='50km']
