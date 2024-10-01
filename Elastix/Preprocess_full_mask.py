import SimpleITK as sitk
import numpy as np
import os
from os.path import join
import matplotlib.pyplot as plt
from my_functions import *
from skimage.util import img_as_ubyte, img_as_float
from scipy import ndimage

#FIXED
root = r'C:\Users\awias\Documents\Research_Assistant\MicroCracks\Data\pRESSURE\NIFTI'
save_folder = r'C:\Users\awias\Documents\Research_Assistant\MicroCracks\Data\Elastix'

file10_avg = 20227
file40_avg = 19197
pixel_diff_avg = file10_avg-file40_avg #This number needs to be added to file40.. I see if this works.

# 1. Indlæs NIfTI-filen
input_file = "Pressure_tests_Scan_2_10_recon"
image = sitk.ReadImage(os.path.join(root,input_file+'.nii')) #join

# 2. Konverter SimpleITK-billedet til et NumPy-array
image_array = sitk.GetArrayFromImage(image)

image_array[image_array > 40000] = 40000
image_array[image_array < 25000] = 25000
 
#Create mask
image_shape = image_array.shape

#Create ones
img = np.zeros(image_shape)

#Get cylinder
img[image_array > 26000] = 1

#Put boundaries so you only get the outline of sample
img[:215,:,:] = 0 #z
img[740:,:,:] = 0 #z
img[:,:220,:] = 0 #y
img[:,740:,:] = 0 #y
img[:,:,:210] = 0 #x
img[:,:,880:] = 0 #x

#Save image
output_file_mask = 'fixed_cropped'
save_nifti(img,os.path.join(save_folder,output_file_mask+'.nii'))
print(f"Image saved as {output_file_mask}.nii")


#Create mask for full picture
mask = np.ones(image_shape)

#Save image
output_file_mask = 'fixed_cropped_mask'
save_nifti(mask,os.path.join(save_folder,output_file_mask+'.nii'))
print(f"Mask saved as {output_file_mask}.nii")


#MOVED
root = r'C:\Users\awias\Documents\Research_Assistant\MicroCracks\Data\pRESSURE\NIFTI'
save_folder = r'C:\Users\awias\Documents\Research_Assistant\MicroCracks\Data\Elastix'

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


#Create mask
image_shape = image_array.shape

#Create ones
img = np.zeros(image_shape)

#Get cylinder
img[image_array > 26000] = 1

#Put boundaries so you only get the outline of sample
img[:215,:,:] = 0 #z
img[740:,:,:] = 0 #z
img[:,:220,:] = 0 #y
img[:,740:,:] = 0 #y
img[:,:,:210] = 0 #x
img[:,:,880:] = 0 #x

#Save image
output_file_mask = 'moved_cropped'
save_nifti(img,os.path.join(save_folder,output_file_mask+'.nii'))
print(f"Image saved as {output_file_mask}.nii")


#Create mask for full picture
mask = np.ones(image_shape)

#Save image
output_file_mask = 'moved_cropped_mask'
save_nifti(mask,os.path.join(save_folder,output_file_mask+'.nii'))
print(f"Mask saved as {output_file_mask}.nii")