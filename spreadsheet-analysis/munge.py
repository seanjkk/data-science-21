# place your code to clean up the data file below.

import csv
import pandas as pd

# Using pandas to read text file, separated by tabs
df = pd.read_csv("data\seoul _realestate.txt", sep = "\t")

# Removing unnecessary columns
df = df[['id', 'buildDate', 'm2', 'min_sales', 'max_sales', 'avg_sales']]

# Dropping rows with NaN values
df = df.dropna()

# Importing to a CSV file in the data folder
df.to_csv(r"data\clean_data.csv", index = False)
