import numpy as np
import pandas as pd

df = pd.read_excel("jogos.xlsx")

df = df.sort_values(by = "Current", ascending=False)

print(df.head(10))

print(df.head(3).agg({'24h Peak': np.sum}))