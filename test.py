#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 14:09:03 2024

@author: andreasaspe
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

tiff_file = '/Volumes/T9/USB/Injection_tracer_test_2D_overnight.ome.tiff'
# tiff_file = '/Volumes/T9/USB/Injection_tracer_test_2D_overnight_high_pressure.ome.tiff'

# Opret en figur og akse
fig, ax = plt.subplots()

def update_frame(frame_num):
    # Åbn TIFF-filen
    with Image.open(tiff_file) as img:
        img.seek(frame_num)
        img_frame = img.copy()  # Kopi af den aktuelle frame

        # Konverter til NumPy array
        img_array = np.array(img_frame)
        img_array_cropped = img_array[70:945+1,115:770-1+6]

        ax.clear()  # Ryd akse
        im = ax.imshow(img_array_cropped, cmap='viridis')
        ax.set_title(f"Frame {frame_num}")

    return [im]

# Opret animation
ani = animation.FuncAnimation(
    fig, 
    update_frame, 
    frames=range(1000, 1500, 100),  # Frames fra 1000 til 1500 med interval 100
    interval=50, 
    blit=True, 
    repeat_delay=1000
)

plt.show()
