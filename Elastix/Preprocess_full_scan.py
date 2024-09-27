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

# 1. Indlæs NIfTI-filen
input_file = "Pressure_tests_Scan_2_10_recon"
image = sitk.ReadImage(os.path.join(root,input_file+'.nii')) #join

# 2. Konverter SimpleITK-billedet til et NumPy-array
image_array = sitk.GetArrayFromImage(image)

# 7. Gem det beskårne billede som en ny NIfTI-fil
output_file = 'fixed_cropped'
sitk.WriteImage(image, os.path.join(save_folder,output_file+'.nii'))

print(f"Cropped image saved as {output_file}.nii")

 
#Create mask
image_shape = image_array.shape

#Create ones
mask = np.zeros(image_shape)

#Get cylinder
mask[image_array > 26000] = 1

#I x-retningen i Slicer skal alt over 880 og alt under 210 være 0.
#I z-retningen er det 740 og 215
#I y-retningen er det 740 og 220

#Put boundaries so you only get the outline of sample
mask[:215,:,:] = 0 #z
mask[740:,:,:] = 0 #z
mask[:,:220,:] = 0 #y
mask[:,740:,:] = 0 #y
mask[:,:,:210] = 0 #x
mask[:,:,880:] = 0 #x

#Save as nifti
mask = sitk.GetImageFromArray(mask)

#Supply with metadata
mask.SetOrigin(image.GetOrigin())
mask.SetSpacing(image.GetSpacing())
mask.SetDirection(image.GetDirection())

#Save image
output_file_mask = 'fixed_cropped_mask'
sitk.WriteImage(mask, os.path.join(save_folder,output_file_mask+'.nii'))
print(f"Mask saved as {output_file_mask}.nii")



#MOVED
root = r'C:\Users\awias\Documents\Research_Assistant\MicroCracks\Data\pRESSURE\NIFTI'
save_folder = r'C:\Users\awias\Documents\Research_Assistant\MicroCracks\Data\Elastix'

# 1. Indlæs NIfTI-filen
input_file = "Pressure_tests_Scan_2_40_recon"
image = sitk.ReadImage(os.path.join(root,input_file+'.nii')) #join

# 2. Konverter SimpleITK-billedet til et NumPy-array
image_array = sitk.GetArrayFromImage(image)

# 7. Gem det beskårne billede som en ny NIfTI-fil
output_file = 'moved_cropped'
sitk.WriteImage(image, os.path.join(save_folder,output_file+'.nii'))

print(f"Cropped image saved as {output_file}.nii")

 
#Create mask
image_shape = image_array.shape

#Create ones
mask = np.zeros(image_shape)

#Get cylinder
mask[image_array > 26000] = 1

#I x-retningen i Slicer skal alt over 880 og alt under 210 være 0.
#I z-retningen er det 740 og 215
#I y-retningen er det 740 og 220

#Put boundaries so you only get the outline of sample
mask[:215,:,:] = 0 #z
mask[740:,:,:] = 0 #z
mask[:,:220,:] = 0 #y
mask[:,740:,:] = 0 #y
mask[:,:,:210] = 0 #x
mask[:,:,880:] = 0 #x

#Save as nifti
mask = sitk.GetImageFromArray(mask)

#Supply with metadata
mask.SetOrigin(image.GetOrigin())
mask.SetSpacing(image.GetSpacing())
mask.SetDirection(image.GetDirection())

#Save image
output_file_mask = 'moved_cropped_mask'
sitk.WriteImage(mask, os.path.join(save_folder,output_file_mask+'.nii'))
print(f"Mask saved as {output_file_mask}.nii")