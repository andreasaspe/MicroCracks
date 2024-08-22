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

tiff_file = 'g:\MicroCracks\Injection_tracer_test_2D_overnight.ome.tiff'
# tiff_file = 'g:\MicroCracks\Injection_tracer_test_2D_overnight_high_pressure.ome.tiff'

# Create a 3D plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

img_counter = 0
i = 0
min_val = []
max_val = []


idx_list = [0,13700]   #idx_list = [0,13700] KANON! Sammenlign de to
images = []

# Åbn TIFF-filen
with Image.open(tiff_file) as img:
    for i in idx_list:
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

        images.append(img_array_cropped)

        # cmap='viridis'

        # fig = plt.figure()
        # im = plt.imshow(img_array_cropped,cmap=cmap, vmin = 4000, vmax = 10000)#vmin = 5513, vmax = 15000) #vmin=5570, vmax = 58631) #vmin er mindste af alle værdier of vmax er max af alle værdier
        # fig.colorbar(im, orientation='vertical')
        # plt.title(i)
        # plt.show()
        # plt.close()




def block_mean_diff(array1, array2, block_size):
    # Sørg for at arrayerne har samme dimensioner
    assert array1.shape == array2.shape, "Arrays must have the same shape"
    
    # Find dimensioner
    rows, cols = array1.shape
    
    # Opret en matrix til at holde forskelle
    diff_array = np.zeros((rows // block_size, cols // block_size))
    
    # Loop over blokke og beregn gennemsnit
    for i in range(0, rows, block_size):
        for j in range(0, cols, block_size):
            block1 = array1[i:i+block_size, j:j+block_size]
            block2 = array2[i:i+block_size, j:j+block_size]
            # Beregn gennemsnitsforskellen af blokken
            diff_array[i // block_size, j // block_size] = abs(np.mean(block1 - block2))
    
    return diff_array



block_size = 12
img_diff = block_mean_diff(images[0], images[1], block_size)

# print(img_diff)

fig, ax = plt.subplots()
cmap = 'viridis'
cax = ax.imshow(img_diff, cmap=cmap)
cbar = fig.colorbar(cax, ax=ax, orientation='vertical')
cbar.set_label('Colorbar Label')  # Optional: Label for the colorbar
plt.show()

img_diff = images[0] - images[1]

fig, ax = plt.subplots()
cmap = 'viridis'
cax = ax.imshow(img_diff, cmap=cmap)
cbar = fig.colorbar(cax, ax=ax, orientation='vertical')
cbar.set_label('Colorbar Label')  # Optional: Label for the colorbar
plt.show()