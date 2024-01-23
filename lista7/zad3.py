# Lista 7, Zadanie 3. 
# Równanie oscylatora harmonicznego z tłumieniem
# i okresową siłą wymuszającą metodą Rungego-Kutty 4 rzędu

import numpy as np
import matplotlib.pyplot as plt
from methods import runge_kutta_4

omega_hat = 2/3
q = 2

def solve(init_time, init_theta, target_time, timestep, A):

    times = np.arange(init_time, target_time, timestep)

    thetas = np.zeros_like(times)
    thetas[0] = init_theta

    omegas = np.zeros_like(times)
    omegas[0] = 0

    for i in range(1, len(times)):

        omega_der = lambda t, omega: A * np.cos(omega_hat * t) - 1/q * omega - np.sin(thetas[i-1])
        k1_omega = timestep * omega_der(times[i-1], omegas[i-1])
        k2_omega = timestep * omega_der(times[i-1] + timestep/2, omegas[i-1] + k1_omega/2)
        k3_omega = timestep * omega_der(times[i-1] + timestep/2, omegas[i-1] + k2_omega/2)
        k4_omega = timestep * omega_der(times[i-1] + timestep, omegas[i-1] + k3_omega)
        omegas[i] = omegas[i-1] + (k1_omega + 2*k2_omega + 2*k3_omega + k4_omega) / 6

        thetas[i] = thetas[i-1] + timestep * omegas[i]

    return thetas, omegas


def plot_theta_trajectory(init_time, init_theta, target_time, timestep, A):

    times = np.arange(init_time, target_time, timestep)

    thetas, _ = solve(init_time, init_theta, target_time, timestep, A)

    plt.plot(times, thetas, "b-", label="Trajektoria kąta")
    plt.legend()


def plot_theta_phase(init_time, init_theta, target_time, timestep, A):

    thetas, omegas = solve(init_time, init_theta, target_time, timestep, A)

    plt.plot(thetas, omegas, "b-", label="Trajektoria fazowa")
    plt.legend()


def plot_combined(init_time, init_theta, target_time, timestep, A):

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plot_theta_trajectory(init_time, init_theta, target_time, timestep, A)

    plt.subplot(1, 2, 2)
    plot_theta_phase(init_time, init_theta, target_time, timestep, A)

    plt.tight_layout()
    plt.show()


# A = 0.5, theta(0) = 0.01
plot_combined(0, 0.01, 100, 0.01, 0.5)

# A = 0.5, theta(0) = 0.3
plot_combined(0, 0.3, 100, 0.01, 0.5)

# A = 1.35, theta(0) = 0.3
plot_combined(0, 0.3, 100, 0.01, 1.35)
