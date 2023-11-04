# Zadanie 9 Lista 2.
import numpy as np
from numpy import linalg as la
from zad8 import inverse

a = np.array(
    [
        [1, 3, -9, 6, 4],
        [2, -1, 6, 7, 1],
        [3, 2, -3, 15, 5],
        [8, -1, 1, 4, 2],
        [11, 1, -2, 18, 7],
    ]
)

print(f"Wyznacznik macierzy: {la.det(a)}")
print(f"Macierz odwrotna: {inverse(a)}")
