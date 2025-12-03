import pandas as pd
import glob
import os

folder = r"temp_1975_2019"

files1 = glob.glob(os.path.join(folder, "temp_clim_plus80_*.txt"))
files2 = glob.glob(os.path.join(folder, "tempT511*.txt"))
files3 = glob.glob(os.path.join(folder, "tempT799*.txt"))
files4 = glob.glob(os.path.join(folder, "tempT1279*.txt"))
files5 = glob.glob(os.path.join(folder, "meanT*.txt"))

print(f"Nombre de fichiers trouvés : {len(files1)}")
print(f"Nombre de fichiers trouvés : {len(files2)}")
print(f"Nombre de fichiers trouvés : {len(files3)}")
print(f"Nombre de fichiers trouvés : {len(files4)}")
print(f"Nombre de fichiers trouvés : {len(files5)}")

df_new = pd.DataFrame(columns=["date", "temp"])

for file in sorted(files1):
    df = pd.read_csv(file, delim_whitespace=True, header=None,)
    df.columns = ["year", "day", "raw_temp", "green_curve"]
    date_str = (str(df["year"].values[0]) + "-01-01")
    temp = df["raw_temp"].values[0]
    df_new.loc[len(df_new)] = {"date": date_str, "temp": temp}
    
for file in sorted(files2):
    df = pd.read_csv(file, delim_whitespace=True, header=None,)
    df.columns = ["year", "day", "raw_temp", "green_curve"]
    date_str = (str(df["year"].values[0])[:4] + "-01-01")
    temp = df["raw_temp"].values[0]
    df_new.loc[len(df_new)] = {"date": date_str, "temp": temp}
    
for file in sorted(files3):
    df = pd.read_csv(file, delim_whitespace=True, header=None,)
    df.columns = ["year", "day", "raw_temp"]
    date_str = (str(df["year"].values[0])[:4] + "-01-01")
    temp = df["raw_temp"].values[0]
    df_new.loc[len(df_new)] = {"date": date_str, "temp": temp}
    
for file in sorted(files4):
    df = pd.read_csv(file, delim_whitespace=True, header=None,)
    df.columns = ["year", "day", "raw_temp"]
    date_str = (str(df["year"].values[0])[:4] + "-01-01")
    temp = df["raw_temp"].values[0]
    df_new.loc[len(df_new)] = {"date": date_str, "temp": temp}
    
for file in sorted(files5):
    df = pd.read_csv(file, delim_whitespace=True, header=None,)
    df.columns = ["year", "day", "raw_temp"]
    date_str = (str(df["year"].values[0])[:4] + "-01-01")
    temp = df["raw_temp"].values[0]
    df_new.loc[len(df_new)] = {"date": date_str, "temp": temp}
        
df_new.columns = ["date", "temp"]
df_new.to_csv("temperature.csv", index=False)
