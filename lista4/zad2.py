# Zadanie 2 Lista 4. 
import matplotlib.pyplot as plt
import numpy as np
from zad1 import newton

def f(x):
    return np.cosh(x) * np.cos(x) - 1

def fprime(x):
    return np.sinh(x) * np.cos(x) - np.cosh(x) * np.sin(x)

def plot():
    x1 = np.linspace(0, 5, 100)
    x = np.linspace(0, 11, 100)

    plt.plot(x1, f(x1), label="f(x)")
    plt.plot(x1, fprime(x1), label="f'(x)")
    plt.legend()
    plt.grid()
    plt.show()

    plt.plot(x, f(x), label="f(x)")
    plt.plot(x, fprime(x), label="f'(x)")
    plt.legend()
    plt.grid()
    plt.show()


print(f"Metoda Newtona. Punkt startowy: 4")
sol, iter, _ = newton(f, fprime, 4, 1e-6, 100, printxs=True)
print(f"Pierwiastek: {sol}")
print(f"Ilość iteracji: {iter}")
print(f"Wartość funkcji: {f(sol)}")
plot()