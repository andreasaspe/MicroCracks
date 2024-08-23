from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
from tqdm import tqdm
import subprocess

#Tiff files
tiff_file = 'g:\MicroCracks\Injection_tracer_test_2D_overnight.ome.tiff'
# tiff_file = 'g:\MicroCracks\Injection_tracer_test_2D_overnight_high_pressure.ome.tiff'

N_avg_images = 20

img_counter = 0
i = 0

idx_list = [0,13700]   #idx_list = [0,13700] KANON! Sammenlign de to
images = []
avg_image = None
start_idx = 0

# Åbn TIFF-filen
with Image.open(tiff_file) as img:
    #Get average image for the first 20 images.
    for i in range(start_idx,start_idx+N_avg_images):
        img.seek(i)  # Skift til den næste frame
        img_frame = img.copy()  # Kopi af den aktuelle frame

        # Konverter til NumPy array
        img_array = np.array(img_frame,dtype=np.float64)
        # print(img_array.shape)
        # img_array[70,:] = 0
        # img_array[945+1,:] = 0
        img_array[:,762] = 0
        img_array[:,120] = 0

        img_array_cropped = img_array[70:945+1,220-1:685+2] #img_array[:,120:762] #Oprindelig cropping (completely cropped) img_array[70:945+1,220-1:685+2]

        if avg_image is None:
            avg_image = img_array_cropped
        else:
            avg_image += img_array_cropped



#Calculate average image
avg_image /= N_avg_images
ref_img = avg_image


