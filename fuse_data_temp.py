#Writen on google colab for better performances
#Quentin
from google.colab import files

#Add output.csv
uploaded = files.upload()

#Add temperature.csv
uploaded = files.upload()

import pandas as pd

data = pd.read_csv("/content/output.csv")
temp = pd.read_csv("/content/temperature.csv")

data.head()

temp.head()

dic = temp.set_index('date')['temp'].to_dict()
print(dic)

data["temp"] = data["time"].map(dic)

data.head()

data.to_csv("data.csv")

