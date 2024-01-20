# Lista 6. Zadanie 2. Całkowanie wzorem Simpsona 
import numpy as np

def integrate(xs, f):

    if len(xs) % 2 == 0:
        raise ValueError("xs must have odd number of elements")
    
    ys = f(xs)

    h = xs[1] - xs[0]

    return h / 3 * (ys[0] + ys[-1] + 4 * np.sum(ys[1:-1:2]) + 2 * np.sum(ys[2:-1:2]))


def f(x):
    return np.cos(2 * np.arccos(x))


xs1 = np.linspace(-1, 1, 3)
xs2 = np.linspace(-1, 1, 5)
xs3 = np.linspace(-1, 1, 7)

int1 = integrate(xs1, f)
int2 = integrate(xs2, f)
int3 = integrate(xs3, f)

print("Całka metodą Simpsona dla 3 węzłów: ", int1)
print("Całka metodą Simpsona dla 5 węzłów: ", int2)
print("Całka metodą Simpsona dla 7 węzłów: ", int3)
