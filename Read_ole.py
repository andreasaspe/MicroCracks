# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:16:10 2024

@author: awias
"""

from PIL import Image
import dxchange
import os
import olefile
import sys
from io import BytesIO
import io


path = 'F:/'
file = 'Injection_tracer_test_2D.txrm'

filename = os.path.join(path,file)

if olefile.isOleFile(filename):
    # open the file with OleFileIO
    ole = olefile.OleFileIO(filename)
else:
    sys.exit('Not an OLE file')
    
#Print all OLE entries
# print(ole.listdir())

arguments = ['ImageData1', 'Image1']
pics = ole.openstream(arguments)
data = pics.read()

with open('output_file.bin', 'wb') as file:
    file.write(data)


image = Image.open(BytesIO(data))
image.show()  # Dette vil vise billedet, hvis det er en gyldig billedfil
    
# bytes_io = io.BytesIO()
# bytes_io.write(data)
# bytes_io.seek(0)
# bin_data = bytes_io.read()

# image = Image.open(BytesIO(data))


# ole = olefile.OleFileIO()

# dxchange.reader.read_txm(filename)

