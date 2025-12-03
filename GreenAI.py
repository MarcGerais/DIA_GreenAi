import xarray as xr
import matplotlib.pyplot as plt

ds = xr.open_dataset(r"C:\Users\quent\Documents\Green AI\973ef39a27234cbf432833b4e450761\global-gridded-annual-glacier-mass-change_1975-76.nc4")

ds_arctic = ds.sel(lat=slice(85, 66))

print(ds_arctic.values)
print()

df = ds_arctic.to_dataframe().reset_index()
df_clean = df.dropna()
print(df_clean.head())

df_plot = df_clean.sort_values(['lat','lon'])

values = df_clean.columns.tolist()
values.pop(0)
values.pop(0)
values.pop(0)
values.pop(-1)
values.pop(-1)
print(values)

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
