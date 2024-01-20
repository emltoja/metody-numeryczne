# Lista 6 Zadanie 5. Obliczanie całki metodą Gaussa-Legendre'a

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.log(x) / (x**2 - 2*x + 2)


# Całkowanie numeryczne metodą gaussa-legendre'a
def integrate(deg):
    xs, ws = np.polynomial.legendre.leggauss(deg)

    ts = ((np.pi - 1) * xs + np.pi + 1) / 2

    ys = f(ts)
    areas = ys * ws

    return (np.pi - 1) / 2 * np.sum(areas)


print(f'Wartość całki dla 2 węzłów: {integrate(2)}')
print(f'Wartość całki dla 4 węzłów: {integrate(4)}')