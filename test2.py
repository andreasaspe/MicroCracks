import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable, get_cmap

# Example data
x_rows = 10
x = np.linspace(0, 1, x_rows)
y = np.arange(1, x_rows + 1)
values = np.random.uniform(7318251, 9793114, x_rows)  # Example values for colormap

# Create line segments for plotting
lines = [np.array([x[i], y[i]]) for i in range(x_rows)]
segments = np.array(lines)

# Normalize values for colormap
norm = Normalize(vmin=7318251, vmax=9793114)
cmap = get_cmap('viridis')  # Choose your colormap

# Create a LineCollection
lc = LineCollection(segments, cmap=cmap, norm=norm, linewidth=2)

# Create a figure and axis
fig, ax = plt.subplots()

# Add LineCollection to the plot
ax.add_collection(lc)

# Set limits and labels
ax.set_xlim(x.min(), x.max())
ax.set_ylim(y.min(), y.max())

# Add a colorbar
sm = ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label('Value')

plt.show()
