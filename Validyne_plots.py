#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 16:56:33 2024

@author: andreasaspe
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# os.chdir("/Users/andreasaspe/Documents/DTU_igen/Videnskabelig Assistent/Data/Data")
os.chdir("G:/MicroCracks")

#Low pressure
col_names = ['Data Counter', 'Seconds', 'Data in mv/v','nan']
df = pd.read_csv('Validyne_SK2_secondtest_overnight.csv',skiprows=3,names=col_names)

df = df.iloc[:,:-1]

x = df['Seconds']
y = df['Data in mv/v']

x = x[y>500]
y = y[y>500]

plt.figure()
plt.plot(x,y)
plt.title('Tryktab 10 bar')
plt.xlabel('Seconds')
plt.ylabel('Pressure (mv/V)')


#High pressure
col_names = ['Data Counter', 'Seconds', 'Data in mv/v','nan']
df = pd.read_csv('Validyne_SK2_secondtest_overnight_high_pressure.csv',skiprows=3,names=col_names)

df = df.iloc[:,:-1]

x = df['Seconds']
y = df['Data in mv/v']

x = x[y>500]
y = y[y>500]

plt.figure()
plt.plot(x,y)
plt.title('Tryktab 65 bar')
plt.xlabel('Seconds')
plt.ylabel('Pressure (mv/V)')