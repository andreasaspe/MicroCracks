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

#Define folder to images. Video name will also be named the same as the last folder
folder_path = r'G:\MicroCracks\Databehandling\Videos\Completely_cropped_diff_image'
#Create folder
print("Creating folder")
os.makedirs(folder_path,exist_ok=True)

ffmpeg_command = [
    'ffmpeg',
    '-framerate', '10', #10 er frames pr. second
    '-i', os.path.join(folder_path, '%d.png'),
    '-c:v', 'libx264',
    '-r', '30',
    '-pix_fmt', 'yuv420p',
    f'{folder_path}.mp4'
]

#Number of image to average
N_avg_images = 20

#Don't touch this
avg_image = None
i=0

#First reference image
with Image.open(tiff_file) as img:
    while i < img.n_frames:
        for j in range(start_idx,start_idx+N_avg_images):
            #Get average image for the first 20 images.
            img.seek(j)  # Skift til den næste frame
            img_frame = img.copy()  # Kopi af den aktuelle frame

            # Konverter til NumPy array
            img_array = np.array(img_frame,dtype=np.float64)

            #Image array cropped
            img_array_cropped = img_array[70:945+1,220-1:685+2] #img_array[:,120:762] #Oprindelig cropping (completely cropped) img_array[70:945+1,220-1:685+2]

            #Save
            if avg_image is None:
                avg_image = img_array_cropped
            else:
                avg_image += img_array_cropped

        if i == 0:
            #Calculate reference image
            avg_image /= N_avg_images
            ref_img = avg_image
        else:
            
        



