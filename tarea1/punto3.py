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

#valores de x calculados desde la restricion de inextensibilidad
x_values = np.sqrt(l**2 - y_values**2)

#derivada de x
dx= -(y_values*v_values)/(np.sqrt(l**2-y_values**2))


T_values = ( v_values**2) * 0.5 * m # Energia cinetica
V_values = (l-x_values)*m*g  # Energia potencial


# Energia total y lagrngiano
E_values = T_values + V_values
L_values = T_values - V_values



# Componentes del momentum
p_y_values = m  * v_values 
p_x_values = m  * dx
# Momentum total
p_t_values =  np.sqrt(p_x_values**2 + p_y_values**2)

# graficas

plt.style.use('seaborn-whitegrid')
# Energias
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t_values, T_values, label='Energia Cinetica (T)', color='blue', linewidth=1.5)
plt.plot(t_values, V_values, label='Energia Potencial (V)', color='green', linewidth=1.5)
plt.plot(t_values, E_values, label='Energia Total (E)', color='red', linewidth=1.5)
plt.xlabel('Tiempo')
plt.ylabel('Energia')
plt.grid(True)
plt.legend(fontsize=16, edgecolor='black', fancybox=True)


#  Lagrangiao 
plt.subplot(2, 1, 2)
plt.plot(t_values, L_values, label='Lagrangiano (L)', color='purple', linewidth=1.5)
plt.xlabel('Tiempo')
plt.ylabel('Lagrangiano')
plt.legend()
plt.grid(True)
plt.legend(fontsize=16, edgecolor='black', fancybox=True)
plt.tight_layout()
plt.show()


# Momentums
plt.figure(figsize=(12, 8))
plt.plot(t_values, p_y_values, label='Momento en y (p_y)', color='cyan', linewidth=1.5)
plt.plot(t_values, p_x_values, label='Momento en x (p_x)', color='magenta', linewidth=1.5)
plt.plot(t_values, p_t_values, label='Momento total (p_t)', color='brown', linewidth=1.5)

plt.xlabel('Tiempo')
plt.ylabel('Magnitud')
plt.grid(True)
plt.legend()

plt.show()


