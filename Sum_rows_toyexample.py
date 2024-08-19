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

tiff_file = '/Users/andreasaspe/Documents/Injection_tracer_test_2D.ome.tiff'

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

        
# Åbn TIFF-filen
with Image.open(tiff_file) as img:
    # Læs hver side/billede i TIFF-filen
    for i in range(img.n_frames):
        print(i)
        img.seek(i)  # Skift til den næste frame
        img_frame = img.copy()  # Kopi af den aktuelle frame
        
        # Konverter til NumPy array
        img_array = np.array(img_frame)
        # img_array[70,:] = 0
        # img_array[945,:] = 0
        # img_array[:,770] = 0
        # img_array[:,115] = 0
        
        img_array_cropped = img_array[70:945,115:770]
        
        # plt.figure()
        # plt.imshow(img_array_cropped)
        
        x_rows = img_array_cropped.shape[0] #Number of x rows
        thesum = np.zeros(x_rows)

        for j in range(x_rows):
            thesum[j] = np.sum(img_array_cropped[j,:])
                
        # plt.figure()
        # plt.plot(thesum)
        
        ax.plot(np.linspace(0,1,x_rows), np.ones(x_rows)*(i+1), thesum, color='blue')
        
        
                
        # if i == 10:
        #     print("BREAAAAK")
        #     ax.set_xlabel('X axis')
        #     ax.set_ylabel('Y axis')
        #     ax.set_zlabel('Z axis')
        #     # ax.legend()
        #     plt.show()
        #     break
        
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
# ax.legend()
plt.show()  
        
        
        # Her kan du gøre hvad du vil med billedet, f.eks. vise det eller gemme det
        # img_frame.show()  # Viser billedet
        
