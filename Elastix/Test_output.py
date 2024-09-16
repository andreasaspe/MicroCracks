from my_functions import *
import numpy as np
import matplotlib.pyplot as plt
import imageio.v3 as imageio
from skimage.draw import disk
# import helper_functions
import scipy.ndimage as ndimagey
import re
from multiprocessing import Pool

# helper_functions.set_style(shift=-8)

from mpl_toolkits.axes_grid1 import make_axes_locatable
import nibabel as nib
import cupy as cp
import cupyx.scipy.ndimage as cu_ndimage
mempool = cp.get_default_memory_pool()
pinned_mempool = cp.get_default_pinned_memory_pool()

# Creates the rotation matrix and translation vector
# I arrived at this through a mix of trail and error and StackOverflow
def create_ridgid_transform(transform_params, center_of_rotation):
    R = nib.eulerangles.euler2mat(transform_params[2],
                                  transform_params[1],
                                  transform_params[0])
    R = np.linalg.inv(R)
    c = np.asarray(center_of_rotation)
    t = np.asarray([transform_params[5], transform_params[4], transform_params[3]])
    offset = -(c - c.dot(R)).dot(np.linalg.inv(R))
    T = t + offset

    return R, T

# It is much faster to use GPU compared to CPU
def rigid_transform_gpu(arr, R, T, gpu_idx=0, cval=0):
    with cp.cuda.Device(gpu_idx):
        tmp = cu_ndimage.affine_transform(cp.asarray(arr), cp.asarray(R),
                                          offset=cp.asarray(T), output_shape=arr.shape,
                                          mode='constant', cval=cval).get()
        mempool.free_all_blocks()
    return tmp

def colorbar(mappable, title=None, format=None, shift=None):
    if shift is not None:
        set_style(shift)
    last_axes = plt.gca()
    ax = mappable.axes
    fig = ax.figure
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    cbar = fig.colorbar(mappable, cax=cax, format=format)
    plt.sca(last_axes)
    if title is not None:
        cbar.set_label(title)
    return cbar


# Read the transformation parameters and the center of rotation from the output of Elastix.

file_path = r'C:\Users\awias\Documents\Research_Assistant\MicroCracks\Elastix\Outputs\\'
transform_params_pattern = re.compile(r'\(TransformParameters (.+?)\)')
center_of_rotation_pattern = re.compile(r'\(CenterOfRotationPoint (.+?)\)')

with open(file_path+'TransformParameters.0.txt') as f:
    print(f'Opening file {file_path}TransformParameters.0.txt')
    text = f.read().replace('\n', '')

fixed_img = load_nifti(r"..\Data\pRESSURE\NIFTI\Pressure_tests_Scan_2_5_recon_cropped.nii")

moved_img = load_nifti(r"..\Data\pRESSURE\NIFTI\Pressure_tests_Scan_2_65_recon_cropped.nii")


plt.imshow(fixed_img[10,:,:])
plt.show()

plt.imshow(moved_img[10,:,:])
plt.show()