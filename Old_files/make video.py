#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 14:09:03 2024

@author: andreasaspe
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation



tiff_file = '/Volumes/T9/USB/Injection_tracer_test_2D_overnight.ome.tiff'
# tiff_file = '/Volumes/T9/USB/Injection_tracer_test_2D_overnight_high_pressure.ome.tiff'

frames = [] # for storing the generated images
fig = plt.figure()

i = 1000
# Åbn TIFF-filen
with Image.open(tiff_file) as img:
    print(img.n_frames)
    # Læs hver side/billede i TIFF-filen
    while i < 1500:
        print(i)
        img.seek(i)  # Skift til den næste frame
        img_frame = img.copy()  # Kopi af den aktuelle frame

        # Konverter til NumPy array
        img_array = np.array(img_frame)

        img_array_cropped = img_array[70:945+1,115:770-1+6]

        cmap = 'viridis'

        frames.append([plt.imshow(img_array_cropped, cmap=cmap, vmin=7318251, vmax = 9793114, animated=True)])

        i+=100

ani = animation.ArtistAnimation(fig, frames, interval=50, blit=True,
                                repeat_delay=1000)
plt.show()