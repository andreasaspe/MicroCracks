import SimpleITK as sitk
import numpy as np
import os
from os.path import join
import matplotlib.pyplot as plt
from my_functions import *

root = r"C:\Users\awias\Documents\Research_Assistant\MicroCracks\Data\pRESSURE\NIFTI"

# 1. Indlæs NIfTI-filen
input_file1 = "Pressure_tests_Scan_2_10_recon"
input_file2 = "Pressure_tests_Scan_2_40_recon"

image1 = sitk.ReadImage(os.path.join(root,input_file1+'.nii')) #join
image2 = sitk.ReadImage(os.path.join(root,input_file2+'.nii')) #join

# 2. Konverter SimpleITK-billedet til et NumPy-array
image_array1 = sitk.GetArrayFromImage(image1)
image_array2 = sitk.GetArrayFromImage(image2)

# 3. Definér cropping-intervallet (x, y, z i Numpy svarer til (z, y, x))
x_start, x_end = 485, 517 #480, 526 Hvis jeg gør det her, så kommer der et meget massivt (lyst) område frem i Slicer.
y_start, y_end = 579, 616 #572, 617 Hvis jeg gør det her, så kommer der et meget massivt (lyst) område frem i Slicer.
z_start, z_end = 528, 550 #450, 528 Hvis jeg gør det her, så kommer der et meget massivt (lyst) område frem i Slicer.

# 4. Crop billedet ved at bruge slicing af NumPy-arrayet
cropped_array1 = image_array1[z_start:z_end, y_start:y_end, x_start:x_end]
cropped_array2 = image_array2[z_start:z_end, y_start:y_end, x_start:x_end]

print(cropped_array1.shape)
print(cropped_array2.shape)

# for i in range(cropped_array1.shape[0]):
#     fig, ax = plt.subplots(nrows=1,ncols=2)

#     ax[0].imshow(cropped_array1[i,:,:],cmap='gray')
#     ax[1].imshow(cropped_array2[i,:,:],cmap='gray')
#     plt.show()


save_folder = r'C:\Users\awias\Documents\Research_Assistant\MicroCracks\Data\test'
save_nifti(cropped_array1,os.path.join(save_folder,'cropped_array1.nii'))
save_nifti(cropped_array2,os.path.join(save_folder,'cropped_array2.nii'))


# diff_img = abs(cropped_array1 - cropped_array2)

# plt.figure()
# plt.imshow(diff_img[:,:,10],cmap='gray')
# plt.show()