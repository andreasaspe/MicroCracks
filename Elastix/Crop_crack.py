import SimpleITK as sitk
import numpy as np
import os
from os.path import join
import matplotlib.pyplot as plt

root = r"D:\MicroCracks\pRESSURE\NIFTI"

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

# 5. Konverter tilbage til SimpleITK-billede
cropped_image = sitk.GetImageFromArray(cropped_array)

# 6. Overfør metadata (origin, spacing, direction) fra det originale billede
cropped_image.SetOrigin(image.GetOrigin())
cropped_image.SetSpacing(image.GetSpacing())
cropped_image.SetDirection(image.GetDirection())

# 7. Gem det beskårne billede som en ny NIfTI-fil
output_file = input_file + '_cropped'
sitk.WriteImage(cropped_image, os.path.join(root,output_file+'.nii'))

print(f"Cropped image saved as {output_file}")