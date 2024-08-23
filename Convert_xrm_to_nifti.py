# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 10:15:22 2024

@author: awias
"""

import xrmreader
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
import os
# from edu.stanford.rsl.conrad.data.numeric import NumericGrid


# import pyconrad.autoinit
# from edu.stanford.rsl.conrad.data.numeric import NumericGrid

file = r'g:\MicroCracks\Injection_tracer_test_2D.txrm'
file = 'g:\MicroCracks\Scan_1_Dry\Scan_1_Dry_2024-07-09_120630\Dry_scan\Scan_1_Dry_Dry_scan.txrm'
# file = 'g:\MicroCracks\pRESSURE\Pressure_tests_Scan_2_5_recon.txm'

# metadata = xrmreader.read_metadata(file)
# print(metadata)

# data = xrmreader.read_txrm(file)
# print(data.shape)

# plt.figure()
# plt.imshow(data[:,200,:])
# plt.show()

# nifti_image = nib.Nifti1Image(data, affine=np.eye(4))

# nib.save(nifti_image, 'output_file2.nii')

# NumericGrid.from_numpy(raw_projections).show('Raw projections')

data_path = r'g:\MicroCracks\pRESSURE'
output_path = r'g:\MicroCracks\pRESSURE\NIFTI'

for filename in os.listdir(data_path):
    data = xrmreader.read_txrm(os.path.join(data_path,filename))
    nifti_image = nib.Nifti1Image(data, affine=np.eye(4))
    filename = file[:-4] + '.nii'
    print("Saving NIFTI")
    nib.save(nifti_image, os.path.join(output_path,filename))
    print("NIFTI saved")