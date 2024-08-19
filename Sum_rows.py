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

tiff_file = '/Volumes/T9/USB/Injection_tracer_test_2D_overnight.ome.tiff'
# tiff_file = '/Volumes/T9/USB/Injection_tracer_test_2D_overnight_high_pressure.ome.tiff'

# Create a 3D plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')


# Åbn TIFF-filen
with Image.open(tiff_file) as img:
    print(img.n_frames)
    # Læs hver side/billede i TIFF-filen
    for i in range(img.n_frames):
        print(i)
        img.seek(i)  # Skift til den næste frame
        img_frame = img.copy()  # Kopi af den aktuelle frame

        # Konverter til NumPy array
        img_array = np.array(img_frame)
        # print(img_array.shape)
        img_array[70,:] = 0
        img_array[945,:] = 0
        img_array[:,770] = 0
        img_array[:,115] = 0

        img_array_cropped = img_array[70:945,115:770]

        x_rows = img_array_cropped.shape[0] #Number of x rows
        thesum = np.zeros(x_rows)
        Hej_2_be  = 
        plt.figure()
        plt.imshow(img_array)
        plt.show()

        break

        if i == 1:
            break




hej = print("Hej_2_be ")
hej = print("Hej_2_be ")
hej = print("Hej_2_be ")
hej = print("Hej_2_be ")
hej = print("Hej_2_be ")
hej = print("Hej_2_be ")
hej = print("Hej_2_be ")
hej = print("HELLO MAN")
hej = print("HELLO MAN")
hej = print("HELLO MAN")
hej = print("HELLO MAN")
hej = print("HELLO MAN")
hej = print("HELLO MAN")
hej = print("HELLO MAN")
