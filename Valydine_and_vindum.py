#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 16:56:33 2024

@author: andreasaspe
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#################################### Validyne #########################################

# os.chdir("/Users/andreasaspe/Documents/DTU_igen/Videnskabelig Assistent/Data/Data")
os.chdir("G:/MicroCracks")

#Low pressure
col_names = ['Data Counter', 'Seconds', 'Data in mv/v','nan']
df = pd.read_csv('Validyne_SK2_secondtest_overnight.csv',skiprows=3,names=col_names)

df = df.iloc[:,:-1]

#Get data
y = df['Data in mv/v']
y = y[y>500]

#Smoothing (running average)
N = 500 #Window size
y = np.convolve(y, np.ones(N)/N, mode='valid')

#Define x (1 datapoint per second)
x = np.arange(len(y))

#Plot
fig, axs = plt.subplots(2,1, figsize=(14, 12))  # 3 rows, 2 columns of subplots

#First figure
axs[0].plot(x,y)
axs[0].set_title('Tryktab 10 bar')
axs[0].set_xlabel('Seconds')
axs[0].set_ylabel('Pressure (mv/V)')


#High pressure
col_names = ['Data Counter', 'Seconds', 'Data in mv/v','nan']
df = pd.read_csv('Validyne_SK2_secondtest_overnight_high_pressure.csv',skiprows=3,names=col_names)

df = df.iloc[:,:-1]

#Get data
y = df['Data in mv/v']
y = y[y>500]

#Smoothing (running average)
N = 1000 #Window size
y = np.convolve(y, np.ones(N)/N, mode='valid')

#Define x (1 datapoint per second)
x = np.arange(len(y))

#Plot
axs[1].plot(x,y)
axs[1].set_title('Tryktab 65 bar')
axs[1].set_xlabel('Seconds')
axs[1].set_ylabel('Pressure (mv/V)')

plt.show()


#Man kan godt gøre sådan også, men jeg laver bare linspace. Jeg ved, at hvert datapunkt er logget hvert sekund.
# x = df['Seconds']
# x = x[y>500]

