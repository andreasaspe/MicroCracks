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
import subprocess

tiff_file = r'C:\Users\awias\Documents\Research_Assistant\MicroCracks\Data\Injection_tracer_test_2D_overnight.ome.tiff'
# tiff_file = r'C:\Users\awias\Documents\Research_Assistant\MicroCracks\Data\Injection_tracer_test_2D_overnight_high_pressure.ome.tiff'

img_counter = 0
i = 0
min_val = []
max_val = []

folder_path = r'C:\Users\awias\Documents\Research_Assistant\MicroCracks\Data\Elastix\2D_images'
#Create folder
print("Creating folder")
os.makedirs(folder_path,exist_ok=True)

cmap='viridis'

#First reference image
with Image.open(tiff_file) as img:
    while i < 100:
            #Get average image for the first 20 images.
            img.seek(i)  # Skift til den næste frame
            img_frame = img.copy()  # Kopi af den aktuelle frame

            # Konverter til NumPy array
            img_array = np.array(img_frame,dtype=np.float64)

            #Image array cropped
            img_array_cropped = img_array[70:945+1,220-1:685+2] #img_array[:,120:762] #Oprindelig cropping (completely cropped) img_array[70:945+1,220-1:685+2]

            #Save
            if i == 0:
                ref_img = img_array_cropped
            else: #Calc diff image
                diff_img = abs(img_array_cropped - ref_img)
                print(diff_img.max())
                fig = plt.figure()
                im = plt.imshow(diff_img,cmap=cmap,vmin = 0, vmax = diff_img.max())#vmin = 5513, vmax = 15000) #1991
                fig.colorbar(im, orientation='vertical')
                plt.title(i)
                plt.show()

            i+=1
            
                # img_counter += 1
