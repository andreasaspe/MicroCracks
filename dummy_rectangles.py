# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:12:28 2024

@author: awias
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches


img_array = np.ones((10,10))

xmin_lim = 1
xmax_lim = 3
ymin_lim = 1
ymax_lim = 4

fig, ax = plt.subplots()
ax.imshow(img_array)
rect = patches.Rectangle((ymin_lim, xmax_lim), ymax_lim-ymin_lim, -(xmax_lim-xmin_lim), linewidth=1, edgecolor='r', facecolor='none') #(koordinaterne for nederste venstre hjørne), bredde, højde
ax.add_patch(rect)
plt.show()

img_array[xmin_lim:xmax_lim,ymin_lim:ymax_lim] = 2


fig, ax = plt.subplots()
ax.imshow(img_array)
rect = patches.Rectangle((ymin_lim, xmax_lim), ymax_lim-ymin_lim, -(xmax_lim-xmin_lim), linewidth=1, edgecolor='r', facecolor='none') #(koordinaterne for nederste venstre hjørne), bredde, højde
ax.add_patch(rect)
plt.show()