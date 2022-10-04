
import csv
import pandas as pd

df = pd.read_csv("data/listings.csv")

# Dropping columns that are empty/mostly empty or might cause errors
drop_columns = ['description', 'neighborhood_overview', 'host_url', 'host_about', 'host_response_time', 'host_response_rate', 'host_acceptance_rate', 'neighbourhood', 'neighbourhood_group_cleansed', 'bathrooms', 'calendar_updated']

df = df.drop(drop_columns, axis=1)

# Dropping rows with null values
df = df.dropna()

df.to_csv(r"data/listings_clean.csv", index = False, encoding="utf-8")
