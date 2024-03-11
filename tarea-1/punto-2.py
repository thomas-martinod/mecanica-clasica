import numpy as np
import matplotlib.pyplot as plt

#Costantes
g = 9.81
l = 3.0
m = 3
# Condiciones iniciales
t0 = 0.0
tf = 5.0
dt = 0.01
y0 = -0.707107*l
v0 =2

# Verlet se explica la matematica en el texto
t_values = np.arange(t0, tf, dt)
y_values = np.zeros_like(t_values)
v_values = np.zeros_like(t_values)
y_values[0] = y0
v_values[0] = v0



def f(t, y, v):
    dydt = v
    denominator = (l**2 - y**2)**0.5
    dvdt = -g * y / denominator
    return dydt, dvdt

for i in range(1, len(t_values)):
    a = f(t_values[i-1], y_values[i-1], v_values[i-1])[1]
    y_values[i] = y_values[i-1] + dt*v_values[i-1] + 0.5*(dt**2)*a
    a_next = f(t_values[i], y_values[i], v_values[i])[1]
    v_values[i] = v_values[i-1] + 0.5*dt*(a + a_next)
    
# calculo del angulo con trigonometria

theta = np.arcsin(y_values/l)

#valores de x calculados desde la restricion de inextensibilidad
x_values = np.sqrt(l**2 - y_values**2)

#derivada de x
dx= -(y_values*v_values)/(np.sqrt(l**2-y_values**2))

# Graficas
# posicion y velocidad
plt.figure(figsize=(10, 6))
plt.plot(t_values, y_values, label='Posición (y)')
plt.plot(t_values, v_values, label='Velocidad (v)')
plt.xlabel('Tiempo')
plt.ylabel('Valores')
plt.legend()
plt.grid(True)
plt.xticks(np.arange(0, tf+0.5, step=0.5))  # Set y-axis grid spacing
plt.show()

# Posicion vs velocidad
plt.figure(figsize=(10, 6))
plt.plot(y_values, v_values)
plt.xlabel('Posición (y)')
plt.ylabel('Velocidad (v)')
plt.title('Posición vs Velocidad')
plt.grid(True)
plt.show()


# Eje 3d de las dos anteriores
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(t_values, y_values, -x_values, color='b', linewidth=2, linestyle='--')
ax.set_zlabel('Posición (x)', fontsize=12)
ax.set_ylabel('Velocidad (v)', fontsize=12)
ax.set_xlabel('Tiempo', fontsize=12)
ax.set_title('Posición vs Velocidad vs Tiempo', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=10)
ax.grid(True)
ax.set_facecolor('white')  # White background
ax.view_init(elev=20, azim=30)  # Adjust the view angle
plt.show()



# Calcular los límites del eje y con un margen adicional
theta_min = min(theta) - 0.1
theta_max = max(theta) + 0.1

# Grafica angulo
plt.figure(figsize=(10, 6))
plt.plot(t_values, theta)
plt.xlabel('Tiempo')
plt.ylabel('Ángulo ($\phi$)')
plt.title('Ángulo en función del tiempo')
plt.ylim(theta_min, theta_max)  # Ajuste manual del eje y con margen adicional
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # Cuadrícula más ligera
plt.show()


# Calcular los límites del eje y con un margen adicional
y_min = min(min(x_values), min(y_values)) - 0.1
y_max = max(max(x_values), max(y_values)) + 0.1

# Grafica posicion x y
plt.figure(figsize=(10, 6))
plt.plot(t_values, x_values, label='Posición en x')
plt.plot(t_values, y_values, label='Posición en y')
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.legend()
plt.grid(True)
plt.xticks(np.arange(0, tf+0.5, step=0.5))
plt.ylim(y_min, y_max)  # Ajuste manual del eje y con margen adicional
plt.show()



