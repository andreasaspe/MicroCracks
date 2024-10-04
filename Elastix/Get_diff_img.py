#This script modifies the 3D image slightly to see if elastix is still able to make them equal...


#Load tiff_file
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from my_functions import *

tiff_file = r"C:\Users\awias\OneDrive - Danmarks Tekniske Universitet\Documents\Research_Assistant\MicroCracks\Data\Elastix\result.0.nii"

fixed_volume = load_nifti(r"C:\Users\awias\OneDrive - Danmarks Tekniske Universitet\Documents\Research_Assistant\MicroCracks\Data\Elastix\fixed_cropped.nii")
moved_volume = load_nifti(r"C:\Users\awias\OneDrive - Danmarks Tekniske Universitet\Documents\Research_Assistant\MicroCracks\Data\Elastix\moved_cropped.nii")
rotated_volume = load_nifti(r"C:\Users\awias\OneDrive - Danmarks Tekniske Universitet\Documents\Research_Assistant\MicroCracks\Data\Elastix\result.0.nii")


# fig, ax = plt.subplots(3, 3, squeeze=False, figsize=(12, 12))
# ax[0, 0].imshow(fixed_volume[200], vmin=np.min(fixed_volume), vmax=np.max(fixed_volume), cmap='gray')
# ax[0, 1].imshow(fixed_volume[:, 200], vmin=np.min(fixed_volume), vmax=np.max(fixed_volume), cmap='gray')
# ax[0, 2].imshow(fixed_volume[:, :, 200], vmin=np.min(fixed_volume), vmax=np.max(fixed_volume), cmap='gray')
# ax[1, 0].imshow(moved_volume[200], vmin=np.min(moved_volume), vmax=np.max(moved_volume), cmap='gray')
# ax[1, 1].imshow(moved_volume[:, 200], vmin=np.min(moved_volume), vmax=np.max(moved_volume), cmap='gray')
# ax[1, 2].imshow(moved_volume[:, :, 200], vmin=np.min(moved_volume), vmax=np.max(moved_volume), cmap='gray')
# ax[2, 0].imshow(rotated_volume[200], vmin=np.min(rotated_volume), vmax=np.max(rotated_volume), cmap='gray')
# ax[2, 1].imshow(rotated_volume[:, 200], vmin=np.min(rotated_volume), vmax=np.max(rotated_volume), cmap='gray')
# ax[2, 2].imshow(rotated_volume[:, :, 200], vmin=np.min(rotated_volume), vmax=np.max(rotated_volume), cmap='gray')
# fig.tight_layout()
# plt.show()

# print("Fixed\n")
# print(np.min(fixed_volume))
# print(np.max(fixed_volume))
# print("Moved\n")
# print(np.min(moved_volume))
# print(np.max(moved_volume))
# print("Rotated\n")
# print(np.min(rotated_volume))
# print(np.max(rotated_volume))


# Diff image
# diff_img = abs(fixed_volume-rotated_volume)

# plt.imshow(diff_img[10,:,:])
# plt.show()

filename = r"C:\Users\awias\OneDrive - Danmarks Tekniske Universitet\Desktop\rotated_volume.nii.gz"

save_nifti(rotated_volume,filename)