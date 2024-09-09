#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 14:10:29 2024

@author: andreasaspe
"""

import nibabel as nib
import os
import matplotlib.pyplot as plt
import numpy as np

data_path = r'/Volumes/T9/MicroCracks/pRESSURE/NIFTI'

file1 = 'Pressure_tests_Scan_2_5_recon'
file2 = 'Pressure_tests_Scan_2_65_recon'

#First file
img_nib1 = nib.load(os.path.join(data_path,file1+'.nii'))

img_data1 = img_nib1.get_fdata()

mask1 = np.ones(img_data1.shape)

mask1[img_data1 < 30000] = 0

nifti_image = nib.Nifti1Image(mask1, affine=np.eye(4))

print("Saving NIFTI")
nib.save(nifti_image, os.path.join(data_path,file1+'_MASK.nii'))
print("NIFTI saved")



#Second file
img_nib2 = nib.load(os.path.join(data_path,file2+'.nii'))

img_data2 = img_nib2.get_fdata()

mask2 = np.ones(img_data2.shape)

mask2[img_data2 < 30000] = 0

nifti_image = nib.Nifti1Image(mask2, affine=np.eye(4))

print("Saving NIFTI")
nib.save(nifti_image, os.path.join(data_path,file2+'_MASK.nii'))
print("NIFTI saved")