import SimpleITK as sitk


# Læs parameterfilen fra elastix
def read_elastix_parameter_file(file_path):
    parameters = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('(TransformParameters'):
                key = 'TransformParameters'
                values = line.strip().split(' ')[1:]
                values[-1] = values[-1][:-1] #Remove parenthasis of last number
                parameters[key] = list(map(float, values))
            elif line.startswith('(Size'):
                key = 'Size'
                values = line.strip().split(' ')[1:]
                values[-1] = values[-1][:-1] #Remove parenthasis of last number
                parameters[key] = list(map(int, values))
            elif line.startswith('(Spacing'):
                key = 'Spacing'
                values = line.strip().split(' ')[1:]
                values[-1] = values[-1][:-1] #Remove parenthasis of last number
                parameters[key] = list(map(float, values))
            elif line.startswith('(Origin'):
                key = 'Origin'
                values = line.strip().split(' ')[1:]
                values[-1] = values[-1][:-1] #Remove parenthasis of last number
                parameters[key] = list(map(float, values))
            elif line.startswith('(CenterOfRotationPoint'):
                key = 'CenterOfRotationPoint'
                values = line.strip().split(' ')[1:]
                values[-1] = values[-1][:-1] #Remove parenthasis of last number
                parameters[key] = list(map(float, values))
            # Tilføj flere parametre, hvis nødvendigt
    return parameters


def apply_euler_transform(input_image_path, output_image_path, parameter_file_path):
    # Load the input image
    input_image = sitk.ReadImage(input_image_path)
    
    #Read parameter_file
    params = read_elastix_parameter_file(parameter_file_path)
    
    # Create an Euler3DTransform
    euler_transform = sitk.Euler3DTransform()
    
    # Set rotation parameters (in radians) and translation
    euler_transform.SetParameters(params['TransformParameters'])
    
    # Set the center of rotation
    euler_transform.SetCenter(params['CenterOfRotationPoint'])
    
    # Apply the transform to the image
    resampled_image = sitk.Resample(input_image, euler_transform, sitk.sitkLinear, 0.0, input_image.GetPixelID())
    
    # Save the transformed image
    sitk.WriteImage(resampled_image, output_image_path)
    print(f"Transformed image saved at {output_image_path}")

input_image_path = r"C:\Users\awias\Documents\Research_Assistant\MicroCracks\Data\Elastix\moved_cropped.nii"
output_image_path = r"C:\Users\awias\Documents\Research_Assistant\MicroCracks\Data\Elastix\transformed.nii"
parameter_file_path = r'C:\Users\awias\Documents\Research_Assistant\MicroCracks\Data\Elastix\Outputs\TransformParameters.0.txt'

# Apply the transformation
apply_euler_transform(input_image_path, output_image_path, parameter_file_path)

