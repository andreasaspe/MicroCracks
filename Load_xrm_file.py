import xrmreader
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
import os


file = r'g:\MicroCracks\Injection_tracer_test_2D.txrm'
# file = 'g:\MicroCracks\Scan_1_Dry\Scan_1_Dry_2024-07-09_120630\Dry_scan\Scan_1_Dry_Dry_scan.txrm'
# file = 'g:\MicroCracks\pRESSURE\Pressure_tests_Scan_2_5_recon.txm'

metadata = xrmreader.read_metadata(file)
# print(metadata)

