import numpy as np
import matplotlib.pyplot as plt


g = 9.81
l = 1.0
theta0 = np.pi / 4
omega0 = 0.0


t0 = 0.0
t_end = 10.0
dt = 0.01

method = input()

def wzor_wahadla(y):
    theta, omega = y
    dydt = np.array([omega, -(g / l) * np.sin(theta)])
    return dydt

def rk4_step(f, y, dt):
    k1 = f(y)
    k2 = f(y + 0.5 * dt * k1)
    k3 = f(y + 0.5 * dt * k2)
    k4 = f(y + dt * k3)
    return y + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
t = t0
y = [theta0, omega0]
angle = [theta0]
trajectory = []

def euler(f, y, dt):
    return y + dt * f(y)
def euler_improved(f, y, dt):
    dydt = f(y)
    omega_new = y[1] + dt * dydt[1]
    theta_new = y[0] + dt * omega_new
    return np.array([theta_new, omega_new])


print("wybierz metode: [euler, eulerimp, rk4]")
while t <= t_end:
    if method == "euler":
        y = euler(wzor_wahadla, y, dt)
    if method == "rk4":
        y = rk4_step(wzor_wahadla, y, dt)
    if method == "eulerimp":
        y = euler_improved(wzor_wahadla, y, dt)



    t += dt
    angle.append(y[0])
    trajectory.append((l * np.sin(y[0]), -l * np.cos(y[0])))

# Konwersja trajektorii na współrzędne kartezjańskie
x = [x[0] for x in trajectory]
y = [y[1] for y in trajectory]

# Wizualizacja trajektorii wahadła
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Trajektoria wahadła RK4")
plt.axis("equal")
plt.grid()
plt.show()
