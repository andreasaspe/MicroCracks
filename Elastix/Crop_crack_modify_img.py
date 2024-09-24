import SimpleITK as sitk
import numpy as np
import os
from os.path import join
import matplotlib.pyplot as plt
from my_functions import *

#FIXED
root = r'C:\Users\awias\Documents\Research_Assistant\MicroCracks\Data\pRESSURE\NIFTI'
save_folder = r'C:\Users\awias\Documents\Research_Assistant\MicroCracks\Data\Elastix'

# 1. Indlæs NIfTI-filen
input_file = "Pressure_tests_Scan_2_5_recon"
image = sitk.ReadImage(os.path.join(root,input_file+'.nii')) #join

# 2. Konverter SimpleITK-billedet til et NumPy-array
image_array = sitk.GetArrayFromImage(image)

# 3. Definér cropping-intervallet (x, y, z i Numpy svarer til (z, y, x))
x_start, x_end = 879, 925
y_start, y_end = 485, 608
z_start, z_end = 436, 467

# 4. Crop billedet ved at bruge slicing af NumPy-arrayet
cropped_array = image_array[z_start:z_end, y_start:y_end, x_start:x_end]

cropped_array = normalize_array(cropped_array,range=[-1000,1000])

# 5. Konverter tilbage til SimpleITK-billede
cropped_image = sitk.GetImageFromArray(cropped_array)

# 6. Overfør metadata (origin, spacing, direction) fra det originale billede
cropped_image.SetOrigin(image.GetOrigin())
cropped_image.SetSpacing(image.GetSpacing())
cropped_image.SetDirection(image.GetDirection())

# 7. Gem det beskårne billede som en ny NIfTI-fil
output_file = 'fixed_cropped'
sitk.WriteImage(cropped_image, os.path.join(save_folder,output_file+'.nii'))

print(f"Cropped image saved as {output_file}.nii")


#Create mask
cropped_shape = cropped_array.shape

#Create ones
mask = np.ones(cropped_shape)

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
input_file = "Pressure_tests_Scan_2_65_recon"
image = sitk.ReadImage(os.path.join(root,input_file+'.nii')) #join

# 2. Konverter SimpleITK-billedet til et NumPy-array
image_array = sitk.GetArrayFromImage(image)

# 3. Definér cropping-intervallet (x, y, z i Numpy svarer til (z, y, x))
x_start, x_end = 879, 925
y_start, y_end = 485, 608
z_start, z_end = 436, 467

# 4. Crop billedet ved at bruge slicing af NumPy-arrayet
cropped_array = image_array[z_start:z_end, y_start:y_end, x_start:x_end]

cropped_array = normalize_array(cropped_array,range=[-1000,1000])

cropped_array[4:10,80:90,30:42] = -1000

# 5. Konverter tilbage til SimpleITK-billede
cropped_image = sitk.GetImageFromArray(cropped_array)

# 6. Overfør metadata (origin, spacing, direction) fra det originale billede
cropped_image.SetOrigin(image.GetOrigin())
cropped_image.SetSpacing(image.GetSpacing())
cropped_image.SetDirection(image.GetDirection())

# 7. Gem det beskårne billede som en ny NIfTI-fil
output_file = 'moved_cropped'
sitk.WriteImage(cropped_image, os.path.join(save_folder,output_file+'.nii'))

print(f"Cropped image saved as {output_file}.nii")


#Create mask
cropped_shape = cropped_array.shape

#Create ones
mask = np.ones(cropped_shape)

#Save as nifti
mask = sitk.GetImageFromArray(mask)

#Supply with metadata
mask.SetOrigin(cropped_image.GetOrigin())
mask.SetSpacing(cropped_image.GetSpacing())
mask.SetDirection(cropped_image.GetDirection())

#Save image
output_file_mask = 'moved_cropped_mask'
sitk.WriteImage(mask, os.path.join(save_folder,output_file_mask+'.nii'))
print(f"Mask saved as {output_file_mask}.nii")