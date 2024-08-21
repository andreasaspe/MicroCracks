import plotly.graph_objects as go
import numpy as np

# Assuming you have grid_x, grid_y, grid_z defined somewhere
# For demonstration, we'll create some example data
grid_x, grid_y = np.meshgrid(np.linspace(0, 1, 100), np.linspace(0, 1, 100))
grid_z = np.sin(grid_x * 2 * np.pi) * np.cos(grid_y * 2 * np.pi)

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
fig.write_html("plot.html")

# Optionally, display the plot in an interactive environment
fig.show()
