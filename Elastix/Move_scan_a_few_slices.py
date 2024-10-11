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

# 1. Indlæs NIfTI-filen
input_file = "Pressure_tests_Scan_2_5_recon"
image = sitk.ReadImage(os.path.join(root,input_file+'.nii')) #join

# 2. Konverter SimpleITK-billedet til et NumPy-array
image_array1 = sitk.GetArrayFromImage(image)

#Get median value
img1_median = np.median(image_array1)




#MOVED
#1. Indlæs NIfTI-filen
input_file = "Pressure_tests_Scan_2_65_recon"
image = sitk.ReadImage(os.path.join(root,input_file+'.nii')) #join

# 2. Konverter SimpleITK-billedet til et NumPy-array
image_array2 = sitk.GetArrayFromImage(image)

# Get median value
img2_median = np.median(image_array2)


#Adjust for median values
if img1_median > img2_median:
    image_array2+=img1_median
else:
    image_array1+=img2_median


#Clamping
image_array1[image_array1 > 40000] = 40000
image_array1[image_array1 < 25000] = 25000

image_array2[image_array2 > 40000] = 40000
image_array2[image_array2 < 25000] = 25000

#Normalising
image_array1 = normalize_array(image_array1,range=[-1000,1000])
image_array2 = normalize_array(image_array2,range=[-1000,1000])

#Move image 1. Dont know if its the correct boundaries?
new_image_array = np.zeros(image_array1.shape)
new_image_array[2:,:-2:,:] = image_array1[:-2,2:,:]

# 7. Gem det beskårne billede som en ny NIfTI-fil
# 1 (new_image_array, fordi jeg skubbede billedet nogle pixels rundt manuelt i stedet for elastix)
output_file = 'fixed_cropped'
save_nifti(new_image_array,os.path.join(save_folder,output_file+'.nii'))
print(f"Cropped image saved as {output_file}.nii")
# 2
output_file = 'moved_cropped'
save_nifti(image_array2,os.path.join(save_folder,output_file+'.nii'))
print(f"Cropped image saved as {output_file}.nii")