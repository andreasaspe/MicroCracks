#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 14:09:03 2024

@author: andreasaspe
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
from tqdm import tqdm
import subprocess


# im = Image.open('/Users/andreasaspe/Documents/Injection_tracer_test_2D.ome.tiff')
# im.show()

# import numpy
# imarray = numpy.array(im)

# tiff_file = '/Volumes/T9/MicroCracks/Injection_tracer_test_2D_overnight.ome.tiff'
# tiff_file = '/Volumes/T9/MicroCracks/Injection_tracer_test_2D_overnight_high_pressure.ome.tiff'

# tiff_file = 'g:\MicroCracks\Injection_tracer_test_2D_overnight.ome.tiff'
tiff_file = 'g:\MicroCracks\Injection_tracer_test_2D_overnight_high_pressure.ome.tiff'

#Change path to ffmpeg executable, since I cannot add it to environmental variable, due to admin rights.
ffmpeg_path = r"c:\ffmpeg"
os.chdir(ffmpeg_path)

# Create a 3D plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

img_counter = 0
i = 0
min_val = []
max_val = []

folder_path = r'G:\MicroCracks\Databehandling\Videos\Completely_cropped_highpressure'
#Create folder
print("Creating folder")
os.makedirs(folder_path,exist_ok=True)

ffmpeg_command = [
    'ffmpeg',
    '-framerate', '10', #10 er frames pr. second
    '-i', os.path.join(folder_path, '%d.png'),
    '-c:v', 'libx264',
    '-r', '30',
    '-pix_fmt', 'yuv420p',
    f'{folder_path}.mp4'
]

#Det her er kommando-formtatet, hvis man kører det fra terminalen
#ffmpeg -framerate 1 -i G:\MicroCracks\Videos\Every_50_image_cropped\%d.png -c:v libx264 -r 30 -pix_fmt yuv420p G:\MicroCracks\Videos\Every_50_image_cropped.mp4

# Åbn TIFF-filen
with Image.open(tiff_file) as img:
    print(img.n_frames)
    # Læs hver side/billede i TIFF-filen
    # for i in range(img.n_frames):
    while i < img.n_frames:

        if img_counter%50 == 0:
            print(i)
        
        img.seek(i)  # Skift til den næste frame
        img_frame = img.copy()  # Kopi af den aktuelle frame

        # Konverter til NumPy array
        img_array = np.array(img_frame)
        # print(img_array.shape)
        # img_array[70,:] = 0
        # img_array[945+1,:] = 0
        # img_array[:,770] = 0
        # img_array[:,115-1+6] = 0

        img_array_cropped = img_array[70:945+1,220-1:685+2]
        # min_val.append(np.min(img_array_cropped))
        # max_val.append(np.max(img_array_cropped))


        cmap='viridis'


        fig = plt.figure()
        im = plt.imshow(img_array_cropped,cmap=cmap, vmin = 4000, vmax = 10000)#vmin = 5513, vmax = 15000) #vmin=5570, vmax = 58631) #vmin er mindste af alle værdier of vmax er max af alle værdier
        fig.colorbar(im, orientation='vertical')
        plt.title(i)
        # plt.show()
        plt.savefig(f"{folder_path}\\{img_counter}.png")
        plt.close()

        i+= 50
        img_counter += 1 #DONT TOUCH


#Creating video
print("Creating video")
subprocess.run(ffmpeg_command, check=True)

#Remove folder again
print("Removing folder")
shutil.rmtree(folder_path)

# print(np.min(min_val))
# print(np.max(max_val))