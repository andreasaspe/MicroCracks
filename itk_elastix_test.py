import itk

print("Hello")


fixed_image = itk.imread('/Volumes/T9/MicroCracks/pRESSURE/NIFTI/Pressure_tests_Scan_2_5_recon.nii')
moving_image = itk.imread('/Volumes/T9/MicroCracks/pRESSURE/NIFTI/Pressure_tests_Scan_2_65_recon.nii')

registered_image, params = itk.elastix_registration_method(fixed_image, moving_image)