import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"]
})

# Define the range of x values
x = np.linspace(-10, 10, 400)

# Define the parameters for the three hyperbolas
A_values = [-1/18, -7/3]  # Adjust the scale of the hyperbolas
B_values = [3, 7+7/3]  # Adjust the horizontal shift of the hyperbolas
colors = ('blue', 'red', 'green')
points = [[[0,3],[6,1]], [[1,7],[2,0]]]  # Points and their coordinates

# Plot each hyperbola
for i in range(len(A_values)):
    y = A_values[i] * x**2 + B_values[i]
    plt.plot(x, y, label=f"$y({points[i][0][0]})={points[i][0][1]}, y({points[i][1][0]}) = {points[i][1][1]}$", color = colors[i])
    plt.scatter([point[0] for point in points[i]], [point[1] for point in points[i]], color=colors[i])

# Add labels and legend
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.ylim((-1, 10))
plt.title(r'Trayectorias parabólicas $y = Ax^2 + B$')
plt.legend()

# Show the plot
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()
