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
# os.chdir("/Volumes/T9/MicroCracks")
# os.chdir("G:/MicroCracks")
os.chdir(r"C:\Users\awias\OneDrive - Danmarks Tekniske Universitet\Documents\Research_Assistant\MicroCracks\Data")


#Low pressure

col_names = ['Data Counter', 'Seconds', 'Data in mv/v','nan']
df = pd.read_csv('Validyne_SK2_secondtest_overnight.csv',skiprows=3,names=col_names)

df = df.iloc[:,:-1]

#Get data
y_lowpressure = df['Data in mv/v']
y_lowpressure = y_lowpressure[y_lowpressure>500]

#Smoothing (running average)
N = 500 #Window size
y_lowpressure = np.convolve(y_lowpressure, np.ones(N)/N, mode='valid')

#Define x (1 datapoint per second)
x_lowpressure = np.arange(len(y_lowpressure))

#Plot
fig, axs = plt.subplots(3,2, figsize=(14, 12))  # 3 rows, 2 columns of subplots

#First figure
# axs[0].plot(x,y)
# axs[0].set_title('Tryktab 10 bar')
# axs[0].set_xlabel('Seconds')
# axs[0].set_ylabel('Pressure (mv/V)')


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
y = y[240:75688+240] #y[0:len(y)-(len(y)-75688)] #Valydine har jeg regnet ud begyndte at logge 4 minutter før vindum pumperne. Så jeg skipper de første 4*60 = 240 sekunder. Og gør den 75688 datapunkter (sekunder) lang fordi så lang er Vindum filen. Så nu burde det passe.
print(len(y))
#Define x (1 datapoint per second)
x = np.arange(len(y))

#Plot
axs[2,0].plot(x,y)
axs[2,0].set_title('Tryktab 65 bar')
axs[2,0].set_xlabel('Seconds')
axs[2,0].set_ylabel('Pressure (mv/V)')



#Man kan godt gøre sådan også, men jeg laver bare linspace. Jeg ved, at hvert datapunkt er logget hvert sekund.
# x = df['Seconds']
# x = x[y>500]

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


#Flow
axs[0,0].plot( df.index , pd.to_numeric(df['P2 Rate']) )
axs[0,0].set_title('FLOW (Tracer injection)')
axs[0,0].set_xlabel('Seconds')
axs[0,0].set_ylabel('Flow rate (mL/m)')

axs[1,0].plot( df.index , pd.to_numeric(df['P3 Rate']) )
axs[1,0].set_title('FLOW (Water injection)')
axs[1,0].set_xlabel('Seconds')
axs[1,0].set_ylabel('Flow rate (mL/m)')


#Pressure
# axs[1,0].plot( df.index , pd.to_numeric(df['P1 Press']) )
# axs[1,0].set_title('PRESSURE (Confining)')
# axs[1,0].set_xlabel('Seconds')
# axs[1,0].set_ylabel('Flow rate (mL/m)')

axs[0,1].plot( df.index , pd.to_numeric(df['P2 Press']) )
axs[0,1].set_title('PRESSURE (Tracer injection)')
axs[0,1].set_xlabel('Seconds')
axs[0,1].set_ylabel('Flow rate (mL/m)')

axs[1,1].plot( df.index , pd.to_numeric(df['P3 Press']) )
axs[1,1].set_title('PRESSURE (Water injection)')
axs[1,1].set_xlabel('Seconds')
axs[1,1].set_ylabel('Flow rate (mL/m)')

axs[2,1].plot( df.index , pd.to_numeric(df['P4 Press']) )
axs[2,1].set_title('PRESSURE (Backpressure)')
axs[2,1].set_xlabel('Seconds')
axs[2,1].set_ylabel('Flow rate (mL/m)')

plt.subplots_adjust(wspace=0.4, hspace=0.4)  # Adjust wspace for horizontal space
fig.suptitle('High pressure',fontsize=20)

plt.show()





#NOW FOR ARTIFICALLY GENERATED LOW PRESSURES
print(len(x_lowpressure))

#Flow tracer
dur1 = 8 #hours. Will be converted to seconds
flow1 = 0.51 #ml/hour. Will be converted to ml/s 
dur2 = 6 #hours. Will be converted to seconds
flow2 = 0 #ml/hour. Will be converted to ml/s 
dur3 = 4 #hours. Will be converted to seconds
flow3 = 2.08 #ml/hour. Will be converted to ml/s 
dur4 = 3 #hours. Will be converted to seconds
flow4 = 0 #ml/hour. Will be converted to ml/s 
dur5 = 2 #hours. Will be converted to seconds
flow5 = 4.08 #ml/hour. Will be converted to ml/s 

y1 = np.ones(dur1*60*60)*(flow1/60) #8 hours
y2 = np.ones(dur2*60*60)*(flow2/60) #8 hours
y3 = np.ones(dur3*60*60)*(flow3/60) #8 hours
y4 = np.ones(dur4*60*60)*(flow4/60) #8 hours
y5 = np.ones(dur5*60*60)*(flow5/60) #8 hours

y_tracer = np.concatenate((y1,y2,y3,y4,y5))


#Flow water
dur1 = 8 #hours. Will be converted to seconds
flow1 = 0 #ml/hour. Will be converted to ml/s 
dur2 = 6 #hours. Will be converted to seconds
flow2 = 0.51 #ml/hour. Will be converted to ml/s 
dur3 = 4 #hours. Will be converted to seconds
flow3 = 0 #ml/hour. Will be converted to ml/s 
dur4 = 3 #hours. Will be converted to seconds
flow4 = 2.08 #ml/hour. Will be converted to ml/s 
dur5 = 2 #hours. Will be converted to seconds
flow5 = 0 #ml/hour. Will be converted to ml/s 

y1 = np.ones(dur1*60*60)*(flow1/60) #8 hours
y2 = np.ones(dur2*60*60)*(flow2/60) #8 hours
y3 = np.ones(dur3*60*60)*(flow3/60) #8 hours
y4 = np.ones(dur4*60*60)*(flow4/60) #8 hours
y5 = np.ones(dur5*60*60)*(flow5/60) #8 hours

y_water = np.concatenate((y1,y2,y3,y4,y5))


fig, axs = plt.subplots(3,1, figsize=(14, 12))  # 3 rows, 2 columns of subplots


y_tracer = y_tracer[:len(y_tracer)-(len(y_tracer)-len(y_lowpressure))] #Cutter flow af, selvom jeg ved det er forkert. Det er for at få det til at passe med, at trykmålingen er kortet af. Trykket er målt i kortere tid end sekvensen rent faktisk er kørt.. Skørt
y_water = y_water[:len(y_water)-(len(y_water)-len(y_lowpressure))]


axs[0].plot(y_tracer)
axs[0].set_title('FLOW (Tracer injection)')
axs[0].set_xlabel('Seconds')
axs[0].set_ylabel('Flow rate (mL/m)')

axs[1].plot(y_water)
axs[1].set_title('FLOW (Water injection)')
axs[1].set_xlabel('Seconds')
axs[1].set_ylabel('Flow rate (mL/m)')

axs[2].plot(x_lowpressure,y_lowpressure)
axs[2].set_title('Tryktab 10 bar')
axs[2].set_xlabel('Seconds')
axs[2].set_ylabel('Pressure (mv/V)')

plt.subplots_adjust(wspace=0.4, hspace=0.4)  # Adjust wspace for horizontal space
fig.suptitle('Low pressure',fontsize=20)

plt.show()
