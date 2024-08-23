import matplotlib.pyplot as plt
import numpy as np
import os
import subprocess
import shutil



#Change path to ffmpeg executable, since I cannot add it to environmental variable, due to admin rights.
ffmpeg_path = r"c:\ffmpeg"
os.chdir(ffmpeg_path)


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
dur6 = 2 #hours. Will be converted to seconds
flow6 = 0 #ml/hour. Will be converted to ml/s 

y1 = np.ones(dur1*60*60)*(flow1/60) #8 hours
y2 = np.ones(dur2*60*60)*(flow2/60) #8 hours
y3 = np.ones(dur3*60*60)*(flow3/60) #8 hours
y4 = np.ones(dur4*60*60)*(flow4/60) #8 hours
y5 = np.ones(dur5*60*60)*(flow5/60) #8 hours
y6 = np.ones(dur6*60*60)*(flow6/60) #8 hours


y_tracer = np.concatenate((y1,y2,y3,y4,y5,y6))



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
dur6 = 2 #hours. Will be converted to seconds
flow6 = 4.08 #ml/hour. Will be converted to ml/s 

y1 = np.ones(dur1*60*60)*(flow1/60) #8 hours
y2 = np.ones(dur2*60*60)*(flow2/60) #8 hours
y3 = np.ones(dur3*60*60)*(flow3/60) #8 hours
y4 = np.ones(dur4*60*60)*(flow4/60) #8 hours
y5 = np.ones(dur5*60*60)*(flow5/60) #8 hours
y6 = np.ones(dur6*60*60)*(flow6/60) #8 hours


y_water = np.concatenate((y1,y2,y3,y4,y5,y6))

print(len(y_water))


folder_path = r'G:\MicroCracks\Databehandling\Videos\Low_pressure_plots'
#Create folder
print("Creating folder")
os.makedirs(folder_path,exist_ok=True)

ffmpeg_command = [
    'ffmpeg',
    '-framerate', '2', #10 er frames pr. second
    '-i', os.path.join(folder_path, '%d.png'),
    '-c:v', 'libx264',
    '-r', '30',
    '-pix_fmt', 'yuv420p',
    f'{folder_path}.mp4'
]

#MAKE PLOTS
i=0
img_counter = 0 #Dont touch
while i < len(y_tracer):
    if i%1000 == 0:
        print(i)
    fig, axs = plt.subplots(2,1, figsize=(14, 12))  # 3 rows, 2 columns of subplots

    axs[0].plot(y_tracer)
    axs[0].scatter(i,y_tracer[i],color='red',s=200)
    # axs[0].axvline(x=5,color='red')
    axs[0].set_title('FLOW (Tracer injection)')
    axs[0].set_xlabel('Seconds')
    axs[0].set_ylabel('Flow rate (mL/m)')

    axs[1].plot(y_water)
    # axs[1].axvline(np.arange(len(y_water))[0],color='red')
    axs[1].scatter(i,y_water[i],color='red',s=200)
    axs[1].set_title('FLOW (Water injection)')
    axs[1].set_xlabel('Seconds')
    axs[1].set_ylabel('Flow rate (mL/m)')

    plt.subplots_adjust(wspace=0.4, hspace=0.4)  # Adjust wspace for horizontal space
    # fig.suptitle('Low pressure',fontsize=20)
    plt.savefig(f"{folder_path}\\{img_counter}.png")
    plt.close()

    i+=250
    img_counter+=1

#Creating video
print("Creating video")
subprocess.run(ffmpeg_command, check=True)

#Remove folder again
print("Removing folder")
shutil.rmtree(folder_path)