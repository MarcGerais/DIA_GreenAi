import pandas as pd
import matplotlib.pyplot as plt

# Use pandas to read the CSV file
df = pd.read_csv('csvs/global-gridded-annual-glacier-mass-change_2021-22.csv')

# Filter the data for the Arctic region (latitude between 66 and 85)
df_arctic = df[(df['lat'] >= 66) & (df['lat'] <= 85)]

print(df_arctic.head())
print()

# Drop rows with missing values
df_clean = df_arctic.dropna()
print(df_clean.head())

# Sort the data by latitude and longitude
df_plot = df_clean.sort_values(['lat', 'lon'])

# Extract column names for further processing
values = df_clean.columns.tolist()
values.pop(0)  # Adjust as needed based on your column structure
values.pop(0)
values.pop(0)
values.pop(-1)
#print(values)

for val in values:
    grid = df_clean.pivot(index='lat', columns='lon', values=val)
    lat = grid.index.values
    lon = grid.columns.values
    values = grid.values
    plt.figure(figsize=(12,6))
    plt.pcolormesh(lon, lat, values, cmap='cividis')
    plt.colorbar(label=val)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title(val)
    plt.show()
