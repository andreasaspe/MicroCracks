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

tiff_file = 'g:\MicroCracks\Injection_tracer_test_2D_overnight.ome.tiff'
# tiff_file = 'g:\MicroCracks\Injection_tracer_test_2D_overnight_high_pressure.ome.tiff'

i = 0
min_val = []
max_val = []

mean_list = []

# Åbn TIFF-filen
with Image.open(tiff_file) as img:
    print(img.n_frames)
    # Læs hver side/billede i TIFF-filen
    # for i in range(img.n_frames):
    while i < img.n_frames:
        
        img.seek(i)  # Skift til den næste frame
        img_frame = img.copy()  # Kopi af den aktuelle frame

        # Konverter til NumPy array
        img_array = np.array(img_frame)
        # print(img_array.shape)
        # img_array[70,:] = 0
        # img_array[90,:] = 0
        # img_array[:,900] = 0
        # img_array[:,880] = 0

        img_array_cropped = img_array[70:90,880:900]

        cmap='viridis'


        # fig = plt.figure()
        # im = plt.imshow(img_array_cropped,cmap=cmap) # vmin = 4000, vmax = 10000 #vmin = 5513, vmax = 15000) #vmin=5570, vmax = 58631) #vmin er mindste af alle værdier of vmax er max af alle værdier
        # fig.colorbar(im, orientation='vertical')
        # plt.title(i)
        # plt.show()
        # plt.close()

        mean = np.mean(img_array_cropped)
        mean_list.append(mean)

        i+= 1

print()