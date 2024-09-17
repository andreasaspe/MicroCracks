#Load tiff_file
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from my_functions import *

tiff_file = r"C:\Users\awias\Documents\Research_Assistant\Data\Elastix\Outputs\result.0.tiff"

fixed_volume = load_nifti(r"C:\Users\awias\Documents\Research_Assistant\Data\pRESSURE\NIFTI\Pressure_tests_Scan_2_5_recon_cropped.nii")
moved_volume = load_nifti(r"C:\Users\awias\Documents\Research_Assistant\Data\pRESSURE\NIFTI\Pressure_tests_Scan_2_65_recon_cropped.nii")

rotated_volume = np.zeros(fixed_volume.shape)
    
with Image.open(tiff_file) as img:
    for i in range(img.n_frames):
        img.seek(i)  # Skift til den næste frame
        rotated_volume[i,:,:] = img

# fig, ax = plt.subplots(3, 3, squeeze=False, figsize=(12, 12))
# ax[0, 0].imshow(fixed_volume[10], vmin=np.min(fixed_volume), vmax=np.max(fixed_volume), cmap='gray')
# ax[0, 1].imshow(fixed_volume[:, 10], vmin=np.min(fixed_volume), vmax=np.max(fixed_volume), cmap='gray')
# ax[0, 2].imshow(fixed_volume[:, :, 10], vmin=np.min(fixed_volume), vmax=np.max(fixed_volume), cmap='gray')
# ax[1, 0].imshow(moved_volume[10], vmin=np.min(moved_volume), vmax=np.max(moved_volume), cmap='gray')
# ax[1, 1].imshow(moved_volume[:, 10], vmin=np.min(moved_volume), vmax=np.max(moved_volume), cmap='gray')
# ax[1, 2].imshow(moved_volume[:, :, 10], vmin=np.min(moved_volume), vmax=np.max(moved_volume), cmap='gray')
# ax[2, 0].imshow(rotated_volume[10], vmin=np.min(rotated_volume), vmax=np.max(rotated_volume), cmap='gray')
# ax[2, 1].imshow(rotated_volume[:, 10], vmin=np.min(rotated_volume), vmax=np.max(rotated_volume), cmap='gray')
# ax[2, 2].imshow(rotated_volume[:, :, 10], vmin=np.min(rotated_volume), vmax=np.max(rotated_volume), cmap='gray')
# fig.tight_layout()
# plt.show()

print("Fixed\n")
print(np.min(fixed_volume))
print(np.max(fixed_volume))
print("Moved\n")
print(np.min(moved_volume))
print(np.max(moved_volume))
print("Rotated\n")
print(np.min(rotated_volume))
print(np.max(rotated_volume))


#Diff image
diff_img = abs(fixed_volume-rotated_volume)

plt.imshow(diff_img[10,:,:])
plt.show()

filename = r"C:\Users\awias\Documents\Research_Assistant\Data\Elastix\Outputs\diff_image.nii.gz"

save_nifti(diff_img,filename)