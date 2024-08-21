# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 10:15:22 2024

@author: awias
"""

import xrmreader
# import pyconrad.autoinit
# from edu.stanford.rsl.conrad.data.numeric import NumericGrid

file = r'g:\MicroCracks\Injection_tracer_test_2D.txrm'
# file = 'F:/Scan_1_Dry/Scan_1_Dry_2024-07-09_120630/Dry_scan/Scan_1_Dry_Dry_scan.txrm'
file = 'g:\MicroCracks\pRESSURE\Pressure_tests_Scan_2_final_recon.txm'

metadata = xrmreader.read_metadata(file)
print(metadata)

# raw_projections = xrmreader.read_txrm(file)

