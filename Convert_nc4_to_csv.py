import os
import xarray as xr
import pandas as pd
from pathlib import Path

# Path to the folder
folder_path = r"C:\Users\quent\Documents\Green AI\973ef39a27234cbf432833b4e450761"

# Path to the folder containing the .nc4 files
input_folder = Path(folder_path)

# Path to the new folder where CSV files will be saved
output_folder = Path(r'C:\Users\quent\Documents\Green AI\csvs')
output_folder.mkdir(parents=True, exist_ok=True)  # Create the folder if it doesn't exist

print("Current working directory:", os.getcwd())

# List all .nc4 files in the folder
nc4_files = [f for f in input_folder.glob('*.nc4')]

# Print the list of files
#print(nc4_files)

for nc4_file in nc4_files:
    try:
        ds = xr.open_dataset(nc4_file)
        df = ds.to_dataframe().reset_index()
        df = df.dropna()
        df = df[df['lat'] >= 66]
        
        output_file = output_folder / f"{nc4_file.stem}.csv"
        print(output_file)
        print()
        df.to_csv(output_file, index=False)  # Save as CSV
        print(f"Successfully converted {nc4_file} to {output_file}")
    
    except Exception as e:
        print(f"Error processing {nc4_file}: {e}")
        