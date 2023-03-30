import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Funkcja opisująca ruch wahadła
def f(t, y, L, g):
    theta, omega = y
    dydt = np.array([omega, -(g / L) * np.sin(theta)])
    return dydt


# Metoda RK4
def RK4(f, t0, y0, tf, h, L, g):
    n = int((tf - t0) / h) + 1
    t = np.linspace(t0, tf, n)
    y = np.zeros((n, len(y0)))
    y[0] = y0
    for i in range(n - 1):
        k1 = h * f(t[i], y[i], L, g)
        k2 = h * f(t[i] + h / 2, y[i] + k1 / 2, L, g)
        k3 = h * f(t[i] + h / 2, y[i] + k2 / 2, L, g)
        k4 = h * f(t[i] + h, y[i] + k3, L, g)
        y[i + 1] = y[i] + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return t, y


# Dane wejściowe
L = 1.0  # Długość wahadła [m]
g = 9.81  # Przyspieszenie ziemskie [m/s^2]
theta0 = np.pi / 4  # Początkowy kąt [rad]
omega0 = 0.0  # Początkowa prędkość kątowa [rad/s]
t0 = 0.0  # Czas początkowy [s]
tf = 10.0  # Czas końcowy [s]
h = 0.01  # Krok czasowy [s]

# Wywołanie metody RK4
t, y = RK4(f, t0, [theta0, omega0], tf, h, L, g)

# Animacja ruchu wahadła
fig, ax = plt.subplots()
line, = ax.plot([], [], 'o-', lw=2)
ax.set_xlim(-1.1 * L, 1.1 * L)
ax.set_ylim(-1.1 * L, 1.1 * L)
ax.set_aspect('equal')
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_title('Animacja ruchu wahadła')


def init():
    line.set_data([], [])
    return line,


def update(frame, y, L, line):
    x = L * np.sin(y[frame, 0])
    y_pos = -L * np.cos(y[frame, 0])
    line.set_data([0, x], [0, y_pos])
    return line,


ani = FuncAnimation(fig, update, frames=len(t), fargs=(y, L, line), init_func=init, blit=True, interval=10)

plt.show()
