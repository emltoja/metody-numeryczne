# Zadanie 3 Lista 4. Prędkość rakiety

import numpy as np
from zad1 import secant


u    = 2510     # Prędkość spalin względem rakiety
m0   = 2.8e6    # Masa rakiety
mdot = 1.33e4   # Szybkość zużycia paliwa
g    = 9.81     # Przyspieszenie ziemskie

def v(t):
    return u * np.log(m0/(m0 - mdot * t)) - g * t


def solvev(vstop):

    tmax = 10
    def f(t): return v(t) - vstop
    
    while np.sign(f(0)) == np.sign(f(tmax)):
        tmax *= 2
    
    return secant(f, 0, tmax, 1e-6, 100)


sol, iter, _ = solvev(335)

print(f"Czas po jakim rakieta osiągnie prędkość 335: {sol}")
print(f"Prędkość w tym momencie: {v(sol)}")
print(f"Ilość iteracji: {iter}")
