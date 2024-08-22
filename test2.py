import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Step 1: Define individual plots (ax1, ax2, ..., ax10)
fig1, axs1 = plt.subplots()
axs1.plot(x, y)
axs1.set_title('Tryktab 10 bar')
axs1.set_xlabel('Seconds')
axs1.set_ylabel('Pressure (mv/V)')

fig2, axs2 = plt.subplots()
axs2.plot(x, np.cos(x))
axs2.set_title('Plot 2')
axs2.set_xlabel('Seconds')
axs2.set_ylabel('Amplitude')

# Repeat for ax3 to ax10...
# For simplicity, we'll just create 3 more plots

fig3, axs3 = plt.subplots()
axs3.plot(x, np.tan(x))
axs3.set_title('Plot 3')

fig4, axs4 = plt.subplots()
axs4.plot(x, np.sin(x) + np.cos(x))
axs4.set_title('Plot 4')

fig5, axs5 = plt.subplots()
axs5.plot(x, np.sin(x) * np.cos(x))
axs5.set_title('Plot 5')

# Step 2: Arrange these plots in a new subplot grid
# For example, a 2x2 grid with axs1, axs3, axs4, and axs5

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs_list = [axs1, axs3, axs4, axs5]
for i, ax in enumerate(axs.flatten()):
    for line in axs_list[i].get_lines():
        ax.add_line(line)
    ax.set_title(axs_list[i].get_title())
    ax.set_xlabel(axs_list[i].get_xlabel())
    ax.set_ylabel(axs_list[i].get_ylabel())
    ax.set_xlim(axs_list[i].get_xlim())
    ax.set_ylim(axs_list[i].get_ylim())

plt.tight_layout()
plt.show()

# Step 3: Rearrange in a different layout
# For example, a 1x2 grid with axs3 and axs5

fig, axs = plt.subplots(1, 2, figsize=(10, 4))

axs_list = [axs3, axs5]
for i, ax in enumerate(axs.flatten()):
    for line in axs_list[i].get_lines():
        ax.add_line(line)
    ax.set_title(axs_list[i].get_title())
    ax.set_xlabel(axs_list[i].get_xlabel())
    ax.set_ylabel(axs_list[i].get_ylabel())
    ax.set_xlim(axs_list[i].get_xlim())
    ax.set_ylim(axs_list[i].get_ylim())

plt.tight_layout()
plt.show()
