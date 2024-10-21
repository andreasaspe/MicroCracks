import SimpleITK as sitk
import numpy as np
import os
from os.path import join
import matplotlib.pyplot as plt
from my_functions import *
from skimage.util import img_as_ubyte, img_as_float
from scipy import ndimage

#FIXED
root = r'C:\Users\awias\OneDrive - Danmarks Tekniske Universitet\Documents\Research_Assistant\MicroCracks\Data\pRESSURE\NIFTI'
save_folder = r'C:\Users\awias\OneDrive - Danmarks Tekniske Universitet\Documents\Research_Assistant\MicroCracks\Data\Elastix'

file10 = 27056 #Value of same pixels in file Pressure_tests_Scan_2_10_recon
file40 = 25648 #Value of same pixels in file Pressure_tests_Scan_2_40_recon

pixel_diff = file10-file40 #This number needs to be added to file40.. I see if this works.

file10_avg = 20227
file40_avg = 19197

pixel_diff_avg = file10_avg-file40_avg #This number needs to be added to file40.. I see if this works.


# 1. Indlæs NIfTI-filen
input_file = "Pressure_tests_Scan_2_10_recon"
image = sitk.ReadImage(os.path.join(root,input_file+'.nii')) #join

# 2. Konverter SimpleITK-billedet til et NumPy-array
image_array = sitk.GetArrayFromImage(image)

# for i in range(10):
#     plt.figure()
#     plt.imshow(image_array[i*10,:,:])
#     plt.show()

image_array[image_array > 40000] = 40000
image_array[image_array < 25000] = 25000

avg = np.mean(image_array)

print(f"Average of 10 is {avg}")

#Normalise
image_array = normalize_array(image_array,range=[-1000,1000])

new_image_array = np.zeros(image_array.shape)
new_image_array[2:,:-1:,2:] = image_array[:-2,1:,:-2]

# 7. Gem det beskårne billede som en ny NIfTI-fil
output_file = 'fixed_cropped'
save_nifti(new_image_array,os.path.join(save_folder,output_file+'.nii'))
print(f"Cropped image saved as {output_file}.nii")





#MOVED
# 1. Indlæs NIfTI-filen
input_file = "Pressure_tests_Scan_2_40_recon"
image = sitk.ReadImage(os.path.join(root,input_file+'.nii')) #join

# 2. Konverter SimpleITK-billedet til et NumPy-array
image_array = sitk.GetArrayFromImage(image)

#Normalise
image_array+=pixel_diff_avg
# image_array = normalize_array(image_array,range=[-1,1])

image_array[image_array > 40000] = 40000
image_array[image_array < 25000] = 25000

avg = np.mean(image_array)

print(f"Average of 40 is {avg}")

#Normalise
image_array = normalize_array(image_array,range=[-1000,1000])

# 7. Gem det beskårne billede som en ny NIfTI-fil
output_file = 'moved_cropped'
save_nifti(image_array,os.path.join(save_folder,output_file+'.nii'))
print(f"Cropped image saved as {output_file}.nii")
 