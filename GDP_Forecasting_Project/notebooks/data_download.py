import collections
import collections.abc
collections.Sequence = collections.abc.Sequence
import wbdata
import pandas as pd
import datetime
import os

# Step 1: Create 'data/' folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Step 2: Define the indicators to fetch
indicators = {
    'NY.GDP.MKTP.KD.ZG': 'GDP Growth Rate (%)',
    'NY.GDP.MKTP.CD': 'GDP (current US$)',
    'NY.GNP.PCAP.CD': 'GNI per capita (current US$)',
    'NE.EXP.GNFS.ZS': 'Exports (% of GDP)',
    'NE.IMP.GNFS.ZS': 'Imports (% of GDP)'
}

# Step 3: Define the date range for data fetching
start_date = datetime.datetime(1960, 1, 1)
end_date = datetime.datetime(2023, 1, 1)

# Step 4: Fetch data for all countries from World Bank
print("Fetching data from World Bank API... This might take a few moments.")
df = wbdata.get_dataframe(indicators, country='all', data_date=(start_date, end_date))

# Step 5: Reset index and clean data
df = df.reset_index()
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['Year'] = df['date'].dt.year

# Step 6: Reorder columns for better readability
indicator_cols = [col for col in df.columns if col not in ['country', 'date', 'Year']]
df = df[['country', 'Year'] + indicator_cols]

# Step 7: Preview the first few rows
print("\nSample data:")
print(df.head())

# Step 8: Save the cleaned raw data to the data folder
save_path = "data/worldbank_gdp_1960_2023.csv"
df.to_csv(save_path, index=False)

print(f"\n✅ File successfully saved at: {save_path}")