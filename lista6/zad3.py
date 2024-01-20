# Lista 6 Zadanie 3. Całkowanie metodą trapezów. 
import numpy as np
import matplotlib.pyplot as plt 
plt.style.use('seaborn-v0_8-darkgrid')

def forg(x):
    return 1/(1 + x**4)

def f(x):
    return 1/(1 + x**(4/3)) 


def integrate(func, lower, upper, num_knots):

    xs = np.linspace(lower, upper, num_knots)
    ys = func(xs)

    deltas = np.diff(xs)
    areas = (ys[:-1] + ys[1:]) * deltas / 2

    return np.sum(areas)



print(integrate(f, 0, 1, 6))


xs = np.linspace(0, 1, 100)
plt.plot(xs, f(xs))
plt.show()

xs2 = np.linspace(1, 10, 100)
plt.plot(xs2, forg(xs2))
plt.show()