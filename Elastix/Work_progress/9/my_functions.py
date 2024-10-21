import numpy as np
import SimpleITK as sitk
import numpy as np

def normalize_array(array, range=[-1, 1]):
    array_min = np.min(array)
    array_max = np.max(array)
    
    # Default range is [-1, 1]
    min_range, max_range = range
    
    # Normalize array to 0-1
    normalized_array = (array - array_min) / (array_max - array_min)
    
    # Scale to the desired range
    scaled_array = normalized_array * (max_range - min_range) + min_range
    
    return scaled_array


def normalize_array(array, range=[-1, 1]):
    array_min = np.min(array)
    array_max = np.max(array)
    
    # Default range is [-1, 1]
    min_range, max_range = range
    
    # Check for the case where array_max == array_min
    if array_max == array_min:
        # If all values are the same, return an array with the min_range value
        return np.full(array.shape, min_range)
    
    # Normalize array to 0-1
    normalized_array = (array - array_min) / (array_max - array_min)
    
    # Scale to the desired range
    scaled_array = normalized_array * (max_range - min_range) + min_range
    
    return scaled_array


def save_nifti(array, filename):
    """
    Save a 2D or 3D NumPy array as a NIFTI file using SimpleITK.

    Parameters:A
    - array: NumPy array (2D or 3D) to be saved.
    - filename: Path to the NIFTI file where the array will be saved.
    """
    # Convert NumPy array to SimpleITK image
    image = sitk.GetImageFromArray(array)
    
    # Save the image as a NIFTI file
    sitk.WriteImage(image, filename)
    
import SimpleITK as sitk

def load_nifti(filename):
    """
    Load a NIFTI file and convert it to a NumPy array using SimpleITK.

    Parameters:
    - filename: Path to the NIFTI file to be loaded.

    Returns:
    - NumPy array representation of the NIFTI file.
    """
    # Read the NIFTI file into a SimpleITK image
    image = sitk.ReadImage(filename)
    
    # Convert the SimpleITK image to a NumPy array
    array = sitk.GetArrayFromImage(image)
    
    return array
