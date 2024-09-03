#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 14:09:03 2024

@author: andreasaspe
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from matplotlib.ticker import FuncFormatter, ScalarFormatter
import pickle
import mpld3
import plotly.graph_objects as go
import matplotlib.patches as patches

#DENNE FIL SUMMERER FRA BUNDEN OG OP, PÅ TVÆRS AF EMNET (originale fil).

# tiff_file = '/Volumes/T9/MicroCracks/Injection_tracer_test_2D_overnight.ome.tiff'
# tiff_file = '/Volumes/T9/MicroCracks/Injection_tracer_test_2D_overnight_high_pressure.ome.tiff'

# tiff_file = 'g:\MicroCracks\Injection_tracer_test_2D_overnight.ome.tiff'
tiff_file = 'g:\MicroCracks\Injection_tracer_test_2D_overnight_high_pressure.ome.tiff'


x_list = []
y_list = []
val_list = []

i = 0
# Åbn TIFF-filen
with Image.open(tiff_file) as img:
    print(img.n_frames)

    while i < img.n_frames:
        print(i)
        img.seek(i)  # Skift til den næste frame
        img_frame = img.copy()  # Kopi af den aktuelle frame

        # Konverter til NumPy array
        img_array = np.array(img_frame)
        xmin_lim = 70
        xmax_lim = 945
        ymin_lim = 190
        ymax_lim = 695

        #Old boundaries
        # xmin_lim = 70  
        # xmax_lim = 945
        # ymin_lim = 115
        # ymax_lim = 775

        img_array_cropped = img_array[xmin_lim:xmax_lim,ymin_lim:ymax_lim]

        # Create figure and axes
        # fig, ax = plt.subplots()
        # ax.imshow(img_array)
        # rect = patches.Rectangle((ymin_lim, xmax_lim), ymax_lim-ymin_lim, -(xmax_lim-xmin_lim), linewidth=1, edgecolor='r', facecolor='none') #(koordinaterne for nederste venstre hjørne), bredde, højde
        # ax.add_patch(rect)
        # plt.show()

        x_rows = img_array_cropped.shape[0] #Number of x rows
        thesum = np.zeros(x_rows)

        for j in range(x_rows):
            thesum[j] = np.sum(img_array_cropped[j,:])

        x = np.linspace(0,1,x_rows)
        y = np.ones(x_rows)*(i+1)

        x_list+=list(x)
        y_list+=list(y)
        val_list+=list(thesum)

        i+=50

x_min, x_max = 0, 1
y_min, y_max = 1, img.n_frames

# Opret gridpunkter
grid_x, grid_y = np.mgrid[0:1:100j, y_min:y_max:100j]

x = np.array([x_list]).squeeze()
y = np.array([y_list]).squeeze()
z = np.array([val_list]).squeeze()

grid_z = griddata((x, y), z, (grid_x, grid_y), method='cubic')

x = grid_x.flatten()
y = grid_y.flatten()
z = grid_z.flatten()

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(grid_x, grid_y, -grid_z, cmap='viridis', edgecolor='none')
# ax.scatter(x,y,z, c=z) #, cmap=cmap, vmin=7318251, vmax = 9793114) cmap=plt.cm.viridis
ax.set_title('Tracing the tracer')
ax.set_xlabel('Length of cell')
ax.set_ylabel('# frames')
ax.set_zlabel('Intensity') #Summed intensity across sample
# ax.set_yticks([0,2000,4000,6000,8000,10000,12000,14000])
# Format the ticks to be in thousands with an exponent
plt.gca().ticklabel_format(axis='y', style='sci', scilimits=(0, 0))


pickle.dump(fig, open('FigureObject.fig.pickle', 'wb')) # This is for Python 3 - py2 may need `file` instead of `open`


# ax.set_xticks([0,1])

# plt.show()

# Create the 3D surface plot
fig = go.Figure(data=[go.Surface(z=grid_z, x=grid_x, y=grid_y, colorscale='Viridis')])

# Update plot layout
fig.update_layout(
    title='Tracing the tracer',
    scene=dict(
        xaxis_title='Length of cell',
        yaxis_title='# frames',
        zaxis_title='Intensity',
    )
)

# Export the plot to an HTML file
# fig.write_html("Injection_tracer_test_2D_overnight_ACROSS_SURFACE.html")
fig.write_html("Injection_tracer_test_2D_overnight_high_pressure_ACROSS_SURFACE.html")

# # Optionally, display the plot in an interactive environment
# fig.show()

