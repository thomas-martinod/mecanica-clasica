import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"]
})

k = 3
x = np.linspace(-5, 5, 100)
y = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x, y)

N = k/Y

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, N, cmap='viridis')

ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.set_zlabel(r'$n(x,y)$')
ax.set_title(r'Índice de refracción $n = k/y$, con $k=3$')

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

