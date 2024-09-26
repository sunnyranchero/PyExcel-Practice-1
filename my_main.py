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
# now we can query this to ask for things between dates. Before we could not.

# Next step is to summarize it using pivot tables.
# Excel has sheets, Pandas has dataframes.

by_product = pd.pivot_table(result, index=["item", "size"], values=["qty"], aggfunc=sum)
# rprint(by_product)

by_country = pd.pivot_table(result, index=["country"], values=["qty"], aggfunc=sum) # how many specific items sold by country.
# rprint(by_country)

# Now how do we export these pivots to csv.
by_product.to_csv(f"{output_path}/by_product.csv") # here we want to include the index because of how the pivot is built above.
by_country.to_csv(f"{output_path}/by_country.csv") 

# Finished 20240925