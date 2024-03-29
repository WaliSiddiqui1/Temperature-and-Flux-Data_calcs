#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 11:50:36 2024

@author: saminakashif
"""

import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import pyproj
import xarray as xr
import csv
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

data = pd.read_csv('/Users/saminakashif/Downloads/asfs30.csv')
print(data.head())
print(data.iloc[1])
selected_columns = data[['datetime', 'temp']]
selected_columns.to_csv("temp_vs_date.csv", index=False)
newdata = pd.read_csv("temp_vs_date.csv")


newdata['datetime'] = pd.to_datetime(newdata['datetime'])

newdata.set_index('datetime', inplace=True)


daily_average_temperature = newdata.resample('D').mean()

print(daily_average_temperature)


fig, ax = plt.subplots()

norm = Normalize(vmin=daily_average_temperature.min(), vmax=daily_average_temperature.max())
cmap = plt.get_cmap('coolwarm') 

for date, temp in zip(daily_average_temperature.index, daily_average_temperature.values):
    color = cmap(norm(temp))
    ax.plot([date], [temp], marker='o', color=color)

sm = ScalarMappable(norm=norm, cmap=cmap)
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label('Temperature (Celsius)')

plt.xlabel("Date")
plt.ylabel('Temperature (Celsius)')
plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
plt.title('Daily Average Temperature')
plt.show()




