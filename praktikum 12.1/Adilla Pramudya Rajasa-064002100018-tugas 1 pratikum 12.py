import pandas as pd

df = pd.read_csv("Negara.csv")

mean = df.groupby(["Benua"]).mean()
std = df.groupby(["Benua"]).std()

print("Berikut Data Framenya: ")
print(df)
print("")
print("Berikut Data Mean: ")
print(mean)
print("")
print("Berikut Data Standard Deviation: ")
print(std)
print("")
