import pandas as pd
import os
import glob
from rich import print as rprint

folder = os.getcwd()
csv_folder = "SourceFiles/csv_files"
full_path = os.path.join(folder, csv_folder)
output_path = os.path.join(folder, "results")
files = glob.glob(full_path + "/*.csv")

data = []

for file in files:
    df = pd.read_csv(file, index_col=None, header=0)
    data.append(df)

result = pd.concat(data, axis=0, ignore_index=True)

# rprint(result.head()) # top 5 of data
# rprint(result.tail()) # bottom 5 of data

if os.path.exists(output_path):
    pass
else:
    os.mkdir(output_path)

# result.to_csv("results/output.csv", index=False) # This will create a new folder and a new csv to store the combined data.

# reviewing data types
rprint(result.dtypes) # need to correct the date into a date rather than an object.

result["date"] = pd.to_datetime(result["date"])
"""
1. Hey, we want to change the date column
2. pass this column in the function. 
3. Then change it and override it with everything as date time.
"""

rprint(result.dtypes)