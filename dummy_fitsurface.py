import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

# Example scatter data
np.random.seed(0)
x = np.random.rand(1000)
y = np.random.rand(1000)
z = np.sin(x * 10) * np.cos(y * 10)

# Define grid points
grid_x, grid_y = np.mgrid[0:1:100j, 0:1:100j]

# Interpolate the data on the grid
grid_z = griddata((x, y), z, (grid_x, grid_y), method='cubic')

# Plotting
fig = plt.figure(figsize=(12, 6))

# Plot original scatter
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(x, y, z, c='r', marker='o')
ax1.set_title('Original Scatter')

# Plot interpolated surface
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(grid_x, grid_y, grid_z, cmap='viridis', edgecolor='none')
ax2.set_title('Fitted Surface')

plt.show()
