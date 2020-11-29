import os
import pandas as pd
from glob import glob


full_table = None
for direc in glob("d*"):
    table = pd.read_csv(f"{direc}/table-1.csv", header=None)
    if os.path.isfile(f"{direc}/table-2.csv"):
        table = pd.concat(
            (table, pd.read_csv(f"{direc}/table-2.csv", header=None)),
            axis=1
        )
        table.columns = list(range(len(table.columns)))
    table.to_csv(f"{direc}/table-full.csv", index=False)
    if full_table is None:
        full_table = table
    else:
        print(full_table.head())
        print(table.head())
        full_table = full_table.append(table, ignore_index=True)

full_table.to_csv("table.csv", index=False)
