#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:23:59 2024

@author: andreasaspe
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# os.chdir("/Users/andreasaspe/Documents/DTU_igen/Videnskabelig Assistent/Data/Data")
# os.chdir("G:/MicroCracks")
os.chdir("/Volumes/T9/MicroCracks")

#Low pressure
# col_names = ['Data Counter', 'Seconds', 'Data in mv/v','nan']
df = pd.read_csv('VindumPumpLog_SK2_secondtest_overnight_high_pressure.csv',sep=';',index_col=False)


# Erstat alle kommaer med prikker i hele DataFrame
df = df.replace(',', '.', regex=True)

columns = ['Date', 'Time', 'P1 Press A', 'P1 Press B', 'P1 Press', 'P1 Rate A', 'P1 Rate B',
           'P1 Rate', 'P1 Vol A', 'P1 Vol B', 'P1 Cum Vol', 'P1 Delta Press', 'P2 Press A',
           'P2 Press B', 'P2 Press', 'P2 Rate A', 'P2 Rate B', 'P2 Rate', 'P2 Vol A', 'P2 Vol B',
           'P2 Cum Vol', 'P2 Delta Press', 'P3 Press A', 'P3 Press B', 'P3 Press', 'P3 Rate A',
           'P3 Rate B', 'P3 Rate', 'P3 Vol A', 'P3 Vol B', 'P3 Cum Vol', 'P3 Delta Press', 'P4 Press A',
           'P4 Press B', 'P4 Press', 'P4 Rate A', 'P4 Rate B', 'P4 Rate', 'P4 Vol A', 'P4 Vol B',
           'P4 Cum Vol', 'P4 Delta Press']

#Er næsten sikker på det er sådan her
#Pumpe 1 er confining
#Pumpe 2 er tracer injection
#Pumpe 3 er vand injection
#Pumpe 4 er backpressure

#Pumperne hedder hhv. P1, P2, P3 og P4.
#Flow er fx. 'P1 Rate'. Dem der hedder noget med A og B tror jeg bare er de to stempler. Det er jeg jo ret ligeglad med.
#Volumen Vol A og B ved jeg ikke om er kummulativt for stempel A og B. Men samlet hedder i hvert fald 'P1 Cum Vol' osv.

fig, axs = plt.subplots(3, 2, figsize=(14, 12))  # 3 rows, 2 columns of subplots

#Flow
axs[0,0].plot( df.index , pd.to_numeric(df['P2 Rate']) )
axs[0,0].set_title('FLOW (Tracer injection)')
axs[0,0].set_xlabel('Seconds')
axs[0,0].set_ylabel('Flow rate (mL/m)')

axs[0,1].plot( df.index , pd.to_numeric(df['P3 Rate']) )
axs[0,1].set_title('FLOW (Water injection)')
axs[0,1].set_xlabel('Seconds')
axs[0,1].set_ylabel('Flow rate (mL/m)')


#Pressure
axs[1,0].plot( df.index , pd.to_numeric(df['P1 Press']) )
axs[1,0].set_title('PRESSURE (Confining)')
axs[1,0].set_xlabel('Seconds')
axs[1,0].set_ylabel('Flow rate (mL/m)')

axs[1,1].plot( df.index , pd.to_numeric(df['P2 Press']) )
axs[1,1].set_title('PRESSURE (Tracer injection)')
axs[1,1].set_xlabel('Seconds')
axs[1,1].set_ylabel('Flow rate (mL/m)')

axs[2,0].plot( df.index , pd.to_numeric(df['P3 Press']) )
axs[2,0].set_title('PRESSURE (Water injection)')
axs[2,0].set_xlabel('Seconds')
axs[2,0].set_ylabel('Flow rate (mL/m)')

axs[2,1].plot( df.index , pd.to_numeric(df['P4 Press']) )
axs[2,1].set_title('PRESSURE (Backpressure)')
axs[2,1].set_xlabel('Seconds')
axs[2,1].set_ylabel('Flow rate (mL/m)')

plt.subplots_adjust(wspace=0.4, hspace=0.4)  # Adjust wspace for horizontal space

plt.show()