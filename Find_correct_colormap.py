#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 14:09:03 2024

@author: andreasaspe
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# im = Image.open('/Users/andreasaspe/Documents/Injection_tracer_test_2D.ome.tiff')
# im.show()

# import numpy
# imarray = numpy.array(im)

tiff_file = '/Volumes/T9/MicroCracks/Injection_tracer_test_2D_overnight.ome.tiff'
# tiff_file = '/Volumes/T9/MicroCracks/Injection_tracer_test_2D_overnight_high_pressure.ome.tiff'

tiff_file = 'g:\MicroCracks\Injection_tracer_test_2D_overnight.ome.tiff'
# tiff_file = 'g:\MicroCracks\Injection_tracer_test_2D_overnight_high_pressure.ome.tiff'


# Create a 3D plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

img_counter = 0
i = 0
min_val = []
max_val = []
# Åbn TIFF-filen
with Image.open(tiff_file) as img:
    print(img.n_frames)
    # Læs hver side/billede i TIFF-filen
    # for i in range(img.n_frames):
    while i < img.n_frames:
        i=8700
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

        img_array_cropped1 = img_array[70:945+1,220-1:685+2]
        # min_val.append(np.min(img_array_cropped))
        # max_val.append(np.max(img_array_cropped))
        # print(img_array_cropped.shape)


        i=10700
        print(i)
        img.seek(i)  # Skift til den næste frame
        img_frame = img.copy()  # Kopi af den aktuelle frame

        # Konverter til NumPy array
        img_array = np.array(img_frame)

        img_array_cropped2 = img_array[70:945+1,220-1:685+2]

        cmap='viridis'

        fig, axs = plt.subplots(1,2)

        axs[0].imshow(img_array_cropped1,cmap=cmap, vmin = 4000, vmax = 10000)#vmin = 5513, vmax = 14000) #vmin=5570, vmax = 58631) #vmin er mindste af alle værdier of vmax er max af alle værdier
        im = axs[1].imshow(img_array_cropped2,cmap=cmap, vmin = 4000, vmax = 10000)#vmin = 5513, vmax = 14000) #vmin=5570, vmax = 58631) #vmin er mindste af alle værdier of vmax er max af alle værdier
        fig.colorbar(im, orientation='vertical')
        plt.show()
        # plt.savefig(f"g:\\MicroCracks\\Videos\\Every_50_image_cropped\\{img_counter}.png")
        plt.close()

        break
        i+= 50
        img_counter += 1 #DONT TOUCH

# print(np.min(min_val))
# print(np.max(max_val))