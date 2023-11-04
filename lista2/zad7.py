# Zadanie 7 Lista 2.
import numpy as np
from numpy import linalg as la
from zad4 import gauss

a = np.array(
    [
        [10, -2, -1, 2, 3, 1, -4, 7],
        [5, 11, 3, 10, -3, 3, 3, -4],
        [7, 12, 1, 5, 3, -12, 2, 3],
        [8, 7, -2, 1, 3, 2, 2, 4],
        [2, -15, -1, 1, 4, -1, 8, 3],
        [4, 2, 9, 1, 12, -1, 4, 1],
        [-1, 4, -7, -1, 1, 1, -1, -3],
        [-1, 3, 4, 1, 3, -4, 7, 6],
    ]
)

b = np.array([0, 12, -5, 3, -25, -26, 9, -7])

solution = gauss(a, b)
print(f"Uzyskane rozwiązanie: {solution}")
print(f"Rozwiązanie z modułu numpy: {la.solve(a, b)}")
