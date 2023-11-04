# Zadanie 6 Lista 2. Układ równań
import numpy as np
from numpy import linalg as la
from zad4 import gauss

a = np.array(
    [
        [3.5, 2.77, -0.76, 1.8],
        [-1.8, 2.68, 3.44, -0.09],
        [0.27, 5.07, 6.9, 1.61],
        [1.71, 5.45, 2.68, 1.71],
    ]
)

b = np.array([7.31, 4.23, 13.85, 11.55])

solution = gauss(a, b)
print(solution)
print(f"Wyznacznik macierzy a: {la.det(a)}")
print(f"Wektor Ax: {np.dot(a, solution)}")
print(f"Oczekwiany wektor wyrazów wolnych: {b}")
