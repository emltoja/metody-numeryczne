# Lista 6 Zadanie 6. Różniczkowanie numeryczne
import numpy as np
import pandas as pd 

def f1(x):
    return x**3 - 2*x

def f2(x):
    return np.sin(x)

def f3(x):
    return np.exp(x)


def D1(f, x, h):
    return (f(x + h) - f(x)) / h


def Dc2(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


def Dc4(f, x, h):
    return (8 * (f(x + h) - f(x - h)) - (f(x + 2 * h) - f(x - 2 * h))) / (12 * h)


f1prim = lambda x : 3*x**2 - 2
f2prim = lambda x : np.cos(x)
f3prim =  lambda x : np.exp(x)

h_values = [0.1, 0.01, 0.001]


data = {
    'h': h_values,
    'f1\'(x)': [f1prim(1)] * len(h_values),
    'D1(f1)':  [f1prim(1) - D1(f1,  1, h) for h in h_values],
    'Dc2(f1)': [f1prim(1) - Dc2(f1, 1, h) for h in h_values],
    'Dc4(f1)': [f1prim(1) - Dc4(f1, 1, h) for h in h_values],
    'f2\'(x)': [f2prim(np.pi/3)] * len(h_values),
    'D1(f2)':  [f2prim(np.pi/3) - D1(f2,  np.pi/3, h) for h in h_values],
    'Dc2(f2)': [f2prim(np.pi/3) - Dc2(f2, np.pi/3, h) for h in h_values],
    'Dc4(f2)': [f2prim(np.pi/3) - Dc4(f2, np.pi/3, h) for h in h_values],
    'f3\'(x)': [f3prim(1)] * len(h_values),
    'D1(f3)':  [f3prim(0) - D1(f3, 0, h) for h in h_values],
    'Dc2(f3)': [f3prim(0) - Dc2(f3, 0, h) for h in h_values],
    'Dc4(f3)': [f3prim(0) - Dc4(f3, 0, h) for h in h_values],
}

df = pd.DataFrame(data).transpose()
print(df)



