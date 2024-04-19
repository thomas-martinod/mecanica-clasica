import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"]
})

# Constante r
r_0 = 2


# Generate meshgrid for x and y
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

# Calculate n for each point on the meshgrid
N = np.sqrt(X**2 + Y**2)/r_0

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(X, Y, N, cmap='viridis')

# Set labels and title
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.set_zlabel(r'$n(x,y)$')
ax.set_title(r'Índice de refracción $n(x,y) = \frac{\sqrt{x^2 + y^2}}{r_0}$, con $r_0 = 2$.')

# Add a color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()
