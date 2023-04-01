import numpy as np
import matplotlib.pyplot as plt

g = 9.81
l = 1.0
theta0 = np.pi / 4
omega0 = 0.0

t0 = 0.0
t_end = 10.0
dt = 0.01
method = input().strip()


def euler(theta, omega, dt):
    theta_new = theta + dt * omega
    omega_new = omega - (dt * g / l) * np.sin(theta)
    return theta_new, omega_new


def euler_improved(theta, omega, dt):
    omega_half = omega - (0.5 * dt * g / l) * np.sin(theta)
    theta_new = theta + dt * omega_half
    omega_new = omega - (dt * g / l) * np.sin(theta_new)
    return theta_new, omega_new


def rk4(theta, omega, dt):
    k1_theta = dt * omega
    k1_omega = dt * (-(g / l) * np.sin(theta))

    k2_theta = dt * (omega + 0.5 * k1_omega)
    k2_omega = dt * (-(g / l) * np.sin(theta + 0.5 * k1_theta))

    k3_theta = dt * (omega + 0.5 * k2_omega)
    k3_omega = dt * (-(g / l) * np.sin(theta + 0.5 * k2_theta))

    k4_theta = dt * (omega + k3_omega)
    k4_omega = dt * (-(g / l) * np.sin(theta + k3_theta))

    theta_new = theta + (k1_theta + 2 * k2_theta + 2 * k3_theta + k4_theta) / 6
    omega_new = omega + (k1_omega + 2 * k2_omega + 2 * k3_omega + k4_omega) / 6

    return theta_new, omega_new


# Główna pętla symulacji
t = t0
theta, omega = theta0, omega0
angle = [theta0]
trajectory = []

while t <= t_end:
    if method == "euler":
        theta, omega = euler(theta, omega, dt)
    elif method == "euler_improved":
        theta, omega = euler_improved(theta, omega, dt)
    elif method == "rk4":
        theta, omega = rk4(theta, omega, dt)
    else:
        print("Nieznana metoda: wybierz 'euler', 'eulerimp' lub 'rk4'")
        method = input().strip()

    t += dt
    angle.append(theta)
    trajectory.append((l * np.sin(theta), -l * np.cos(theta)))

# Konwersja trajektorii na współrzędne kartezjańskie
trajectory = np.array(trajectory)
x = trajectory[:, 0]
y = trajectory[:, 1]

# Wizualizacja trajektorii wahadła
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Trajektoria wahadła")
plt.axis("equal")
plt.grid()
plt.show()
