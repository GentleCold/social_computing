import pandas as pd

# 读取 CSV 数据集
df = pd.read_csv("./data/output_au.csv")

print(df["est"].mean())
print(df.describe())

df = pd.read_csv("./data/output_ca.csv")

print(df["est"].mean())
print(df.describe())

df = pd.read_csv("./data/output_in.csv")

print(df["est"].mean())
print(df.describe())
