import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"]
})

x = np.linspace(-10, 10, 400)

k = 3
A_values = [11, -7/2]
B_values = [130/9, 125/36]
colors = ('blue', 'red', 'green')
points = [[[-2,7],[0,3]], [[1,5],[6,5]]]

for i in range(len(A_values)):
    y = np.sqrt(k**2 * B_values[i] - (x + A_values[i])**2)
    plt.plot(x, y, label=f"$y({points[i][0][0]})={points[i][0][1]}, y({points[i][1][0]}) = {points[i][1][1]}$", color = colors[i])
    plt.scatter([point[0] for point in points[i]], [point[1] for point in points[i]], color=colors[i])

plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.title(r'Trayectorias circulares $y = + \sqrt{k^2B - (x+A)^2}$, con $k=3$.')
plt.ylim((0, 15))
plt.legend()

plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()
