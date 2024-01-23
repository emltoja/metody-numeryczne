# Lista 7, Zadanie 2.
# Rozwiązywanie równań różniczkowych metodami:
# 1) Eulera
# 2) Rungego-Kutty 4 rzędu

import numpy as np
import matplotlib.pyplot as plt
from methods import euler_method, runge_kutta_4

init_arg = 0
init_val = 1

target_arg = 0.5

timestep = 0.1
derivative = lambda x, y: np.sin(y)


x = np.arange(init_arg, target_arg, timestep)
euler_y = np.array([euler_method(derivative, init_arg, init_val, arg, timestep) for arg in x])
runge_y = np.array([runge_kutta_4(derivative, init_arg, init_val, arg, timestep) for arg in x])
plt.plot(x, euler_y, "r--", label="Rozwiązanie metodą eulera")
plt.plot(x, runge_y, "b-", label="Rozwiązanie metodą Rungego-Kutty 4 rzędu")
plt.legend()
plt.show()
