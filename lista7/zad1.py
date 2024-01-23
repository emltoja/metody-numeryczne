# Lista 7, Zadanie 1.
# Rozwiązywanie równań różniczkowych metodami: 
# 1) Eulera
# 2) Rungego-Kutty 2 rzędu
# 3) Rungego-Kutty 4 rzędu

import numpy as np
from methods import euler_method, runge_kutta_2, runge_kutta_4

init_arg = 0
init_val = 1

target_arg = 0.03

timesteps = (target_arg - init_arg) / np.array([1, 2, 4])

solution = lambda x: 31/32 * np.exp(-4*x) + 1/32 * x**2 - 1/8 * x + 1/32

for method in [euler_method, runge_kutta_2, runge_kutta_4]: 
    print(f"Metoda: {method.__name__}")
    print("****")
    for timestep in timesteps: 
        target_val = method(lambda x, y: x**2 - 4*y, init_arg, init_val, target_arg, timestep)
        print(f"Krok: {timestep}, wynik: {target_val}")
        print(f"Błąd: {abs(target_val - solution(target_arg)) / solution(target_arg) * 100:.5f}%")
        
        print("-----------------------------------------------")
    print("===================================================")


print(f"Rozwiązanie dokładne: {solution(target_arg)}")