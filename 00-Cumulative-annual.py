# -*- coding: utf-8 -*-
"""
Created on Wed May 22 23:01:45 2024
@author: Vempi
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load your data
df = pd.read_csv('E:/Downloads/Pamarayan-debit-hujan.csv', index_col=0) 

# Convert 'date' column to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Add a year column
df['year'] = df.index.year

# Group by year and calculate cumulative sum
cumrain = df.groupby('year')['Rainfall'].cumsum().reset_index()
cumrain.set_index('Date', inplace=True)
cumrain['year'] = cumrain.index.year
cumrain['DOY'] = cumrain.index.dayofyear

# Plot cumulative daily rainfall for each year
plt.figure(figsize=(10, 6))
for year in cumrain['year'].unique():
    subset = cumrain[cumrain['year'] == year]
    plt.plot(subset['DOY'], subset['Rainfall'], label=year)

plt.xlabel('Date')
plt.ylabel('Cumulative Rainfall (mm)')
plt.title('Cumulative Daily Rainfall by Year')
plt.legend(title='Year')
plt.show()

