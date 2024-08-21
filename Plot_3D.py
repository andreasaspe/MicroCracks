#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 14:09:03 2024

@author: andreasaspe
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata


# im = Image.open('/Users/andreasaspe/Documents/Injection_tracer_test_2D.ome.tiff')
# im.show()

# import numpy
# imarray = numpy.array(im)

tiff_file = '/Volumes/T9/MicroCracks/Injection_tracer_test_2D_overnight.ome.tiff'
# tiff_file = '/Volumes/T9/MicroCracks/Injection_tracer_test_2D_overnight_high_pressure.ome.tiff'

tiff_file = 'g:\MicroCracks\Injection_tracer_test_2D_overnight.ome.tiff'
# tiff_file = 'g:\MicroCracks\Injection_tracer_test_2D_overnight_high_pressure.ome.tiff'


# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x_list = []
y_list = []
val_list = []

i = 1000
# Åbn TIFF-filen
with Image.open(tiff_file) as img:
    print(img.n_frames)
    # Læs hver side/billede i TIFF-filen
    # for i in range(img.n_frames):
    while i < 14000:
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

        img_array_cropped = img_array[70:945+1,115:770-1+6]

        # plt.figure()
        # plt.imshow(img_array_cropped)


        x_rows = img_array_cropped.shape[0] #Number of x rows
        thesum = np.zeros(x_rows)

        for j in range(x_rows):
            thesum[j] = np.sum(img_array_cropped[j,:])

        x = np.linspace(0,1,x_rows)
        y = np.ones(x_rows)*(i+1)

        cmap='viridis'
        # cax = ax.scatter(x, y, thesum, cmap=plt.cm.viridis, c=thesum) #, cmap=cmap, vmin=7318251, vmax = 9793114)
        # fig.colorbar(cax)

        x_list+=list(x)
        y_list+=list(y)
        val_list+=list(thesum)

        i+=50

    
        
        # if i == 0:
        #     img_array1 = img_array_cropped
        # if i == 100:
        #     img_array2 = img_array_cropped
        #     break

x_min, x_max = 0, 1
y_min, y_max = 1, img.n_frames

# Opret gridpunkter
grid_x, grid_y = np.mgrid[0:1:100j, y_min:y_max:100j]

x = np.array([x_list]).squeeze()
y = np.array([y_list]).squeeze()
z = np.array([val_list]).squeeze()


grid_z = griddata((x, y), z, (grid_x, grid_y), method='cubic')


# ax.set_xlabel('Length of cell')
# ax.set_ylabel('Time')
# ax.set_zlabel('Intensity') #Summed intensity across sample
# # ax.set_xticks([0,1])

# plt.show()

x = grid_x.flatten()
y = grid_y.flatten()
z = grid_z.flatten()

ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(grid_x, grid_y, grid_z, cmap='viridis', edgecolor='none')
# x_norm = (x - x.min()) / (x.max() - x.min())
# y_norm = (y - y.min()) / (y.max() - y.min())
# z_norm = (z - z.min()) / (z.max() - z.min())



# cax = ax.scatter(x,y,z, c=z) #, cmap=cmap, vmin=7318251, vmax = 9793114) cmap=plt.cm.viridis
ax.set_title('Fitted Surface')
ax.set_xlabel('Length of cell')
ax.set_ylabel('Time')
ax.set_zlabel('Intensity') #Summed intensity across sample
# ax.set_xticks([0,1])

# np.save('x',x)
# np.save('y',y)
# np.save('z',z)


plt.show()


# # Plot interpolated surface
# ax2 = fig.add_subplot(122, projection='3d')
# ax2.plot_surface(x_list, y_list, val_list, cmap='viridis', edgecolor='none')
# ax2.set_title('Fitted Surface')
# plt.show()


# def block_mean_diff(array1, array2, block_size):
#     # Sørg for at arrayerne har samme dimensioner
#     assert array1.shape == array2.shape, "Arrays must have the same shape"
    
#     # Find dimensioner
#     rows, cols = array1.shape
    
#     # Opret en matrix til at holde forskelle
#     diff_array = np.zeros((rows // block_size, cols // block_size))
    
#     # Loop over blokke og beregn gennemsnit
#     for i in range(0, rows, block_size):
#         for j in range(0, cols, block_size):
#             block1 = array1[i:i+block_size, j:j+block_size]
#             block2 = array2[i:i+block_size, j:j+block_size]
#             # Beregn gennemsnitsforskellen af blokken
#             diff_array[i // block_size, j // block_size] = np.mean(block1 - block2)
    
#     return diff_array


# block_size = 6
# img_diff = block_mean_diff(img_array1, img_array2, block_size)

# print(img_diff)

# fig, ax = plt.subplots()
# cmap = 'viridis'
# cax = ax.imshow(img_diff, cmap=cmap, vmin=0, vmax = 70000)
# cbar = fig.colorbar(cax, ax=ax, orientation='vertical')
# cbar.set_label('Colorbar Label')  # Optional: Label for the colorbar
# plt.show()