from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
import subprocess

#Tiff files
tiff_file = r'C:\Users\awias\Documents\Research_Assistant\MicroCracks\Data\Injection_tracer_test_2D_overnight.ome.tiff'
# tiff_file = r'C:\Users\awias\Documents\Research_Assistant\MicroCracks\Data\Injection_tracer_test_2D_overnight_high_pressure.ome.tiff'

#Change path to ffmpeg executable, since I cannot add it to environmental variable, due to admin rights.
ffmpeg_path = r"c:\ffmpeg"
os.chdir(ffmpeg_path)

#Define folder to images. Video name will also be named the same as the last folder
folder_path = r'C:\Users\awias\Documents\Research_Assistant\MicroCracks\Data\Databehandling\Videos\non-average'
#Create folder
print("Creating folder")
os.makedirs(folder_path,exist_ok=True)

ffmpeg_command = [
    'ffmpeg',
    '-framerate', '15', #dette tal er er frames pr. second
    '-i', os.path.join(folder_path, '%d.png'),
    '-c:v', 'libx264',
    '-r', '30',
    '-pix_fmt', 'yuv420p',
    f'{folder_path}.mp4'
]

#Number of image to average
N_avg_images = 20

#More definitions
increment = 20
i=0 #Start idx
img_counter = 0 #DONT TOUCH
min_val = []
max_val = []

cmap='viridis'

avg_img = None #For reference image only

#First reference image
with Image.open(tiff_file) as img:
    
    end_number = img.n_frames #Define end of loop
    N_avg_images = 20 #Number of average images for ref
    
    while i < end_number: #img.n_frames:
        
        if i == 0:
            print("Doing ref image")
            for j in range(N_avg_images):
                #Get average image for the first 20 images.
                img.seek(j)  # Skift til den næste frame
                img_frame = img.copy()  # Kopi af den aktuelle frame

                # Konverter til NumPy array
                img_array = np.array(img_frame,dtype=np.float64)

                #Image array cropped
                img_array_cropped = img_array[70:945+1,220-1:685+2] #img_array[:,120:762] #Oprindelig cropping (completely cropped) img_array[70:945+1,220-1:685+2]

                #Save
                if avg_img is None:
                    avg_img = img_array_cropped
                else:
                    avg_img += img_array_cropped
            
            #Calc ref image
            avg_img /= N_avg_images
            ref_img = avg_img
            
            #Update counter
            i=j
        else:
            print(f"Processing {i}/{end_number}")
            #Get average image for the first 20 images.
            img.seek(i)  # Skift til den næste frame
            img_frame = img.copy()  # Kopi af den aktuelle frame

            # Konverter til NumPy array
            img_array = np.array(img_frame,dtype=np.float64)

            #Image array cropped
            img_array_cropped = img_array[70:945+1,220-1:685+2] #img_array[:,120:762] #Oprindelig cropping (completely cropped) img_array[70:945+1,220-1:685+2]

            diff_img = abs(img_array_cropped - ref_img)
            fig = plt.figure()
            im = plt.imshow(diff_img,cmap=cmap,vmin = 0, vmax = 772) #vmin = 5513, vmax = 15000) #1991 3799 er max max value,  772 er mean max value, 0 er mean min value.
            fig.colorbar(im, orientation='vertical')
            plt.title(i)
            plt.savefig(f"{folder_path}\\{img_counter}.png")
            # plt.show()
            plt.close()

            img_counter += 1
            
            min_val.append(np.min(diff_img))
            max_val.append(np.max(diff_img))
            
        i+=1
        

#Creating video
print("Creating video")
subprocess.run(ffmpeg_command, check=True)

#Remove folder again
print("Removing folder")
shutil.rmtree(folder_path)      

print(np.mean(min_val))
print(np.mean(max_val))