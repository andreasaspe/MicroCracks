from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np



# Some dummy data
xval = np.random.randn(10000)
yval = np.random.randn(10000)
zval = np.exp( - (xval**2 + yval**2)/0.5)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

cax = ax.scatter(xval, yval, zval, cmap=plt.cm.viridis, c=zval) 
fig.colorbar(cax)

# plt.show(block=False)
# plt.pause(2)

plt.show()
plt.pause()