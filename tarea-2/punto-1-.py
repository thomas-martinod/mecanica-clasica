import numpy as np
import matplotlib.pyplot as plt
from sympy import *
init_printing()

# Graph settings
gray = '#757575'  # Define a gray color for use in graph settings
plt.rcParams["mathtext.fontset"] = "cm"  # Set the font type for mathematical expressions
plt.rcParams["text.color"] = gray  # Set the text color in the graph
plt.rcParams["font.size"] = 12  # Set the font size in the graph
plt.rcParams["xtick.color"] = gray  # Set the color of the tick marks on the x-axis
plt.rcParams["ytick.color"] = gray  # Set the color of the tick marks on the y-axis
plt.rcParams["axes.labelcolor"] = gray  # Set the color of the axis labels
plt.rcParams["axes.edgecolor"] = gray  # Set the color of the axis edges
plt.rcParams["axes.spines.right"] = False  # Hide the right border of the graph
plt.rcParams["axes.spines.top"] = False  # Hide the top border of the graph

x = symbols('x')  # Define the symbolic variable x
q = pi**4 * sin(pi*x)  # Define a function q
u_e = sin(pi * x)  # Define the analytical solution u_e

def plot_expr(expr, x, title, range=(0, 1), ax=None, linestyle="solid"):
    """Plot SymPy expressions that depend on a variable"""
    expr_num = lambdify(x, expr, "numpy")  # Convert the symbolic expression into a numerical function
    x_num = np.linspace(range[0], range[1], 301)  # Create a range of values for x
    if ax is None:
        plt.figure()  # Create a new figure if no axis is provided
        ax = plt.gca()  # Get the current axis
    ax.plot(x_num, expr_num(x_num), linestyle=linestyle)  # Plot the expression
    ax.set_title(title)  # Set the title of the graph

# Define a basis function for the approximation
def basis_function(x, k):
    """k-th element of the basis"""
    return x*(x-1)*x**k

# Define a function for the approximation
def approx_function(x, num):
    c = symbols('c0:%d'%num)  # Define a symbol for the coefficients c
    u_n = sum([c[k]*basis_function(x, k) for k in range(num)])  # Calculate the approximation of u
    return u_n, c

# Define a function for the residual of the problem
def functional(u, x):
    """Residual for the problem of interest"""
    return integrate((1/2)*(diff(u, x, 2))**2 - q*u, (x, 0, 1))

nterms = 3  # Number of terms for the approximation
u, c = approx_function(x, nterms)  # Calculate the approximation of u and the coefficients c
J = expand(functional(u, x))  # Expand the residual
factor(J)  # Factorize the residual

eqs1 = Matrix([functional(u, x)])  # Convert the residual into a matrix
eqs = Matrix([functional(u, x)]).jacobian(c)  # Calculate the Jacobian matrix
sol = solve(eqs, c)  # Solve the system of equations for the coefficients c
u.subs(sol)  # Calculate the approximation of u with the solved coefficients c

# Plot the analytical and approximate solutions
plt.figure()
ax = plt.gca()
plot_expr(u_e, x, "Ritz vs Analytical Solution", ax=ax)
plot_expr(u.subs(sol), x, "Ritz vs Analytical Solution", ax=ax, linestyle="dashed")
plt.legend(["Exact", "Ritz"])  # Add a legend to the graph
plt.show()  # Show the graph

# Calculate the relative error
err = integrate((u_e - u.subs(sol))**2, (x, 0, 1))/integrate(u_e**2, (x, 0, 1))
print(N(sqrt(err)*100))  # Print the relative error