# Zadanie 1 Lista 2. Uwarunkowanie macierzy
import numpy as np
from numpy import linalg as la

def print_info(subex: str, mat):
    print(f'=====PODPUNKT {subex.capitalize()}==========')
    print(f'Wyznacznik macierzy A: {la.det(mat)}')
    print(f'Współczynnik uwarunkowania macierzy A: {la.cond(mat, 2)}')
    print('=========================')

# Podpunkt a
a1 = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
print_info('A', a1)

# Podpunkt b
a2 = np.array([[2.11, -0.8, 1.72], [-1.84, 3.03, 1.29], [-1.57, 5.25, 4.3]])
print_info('B', a2)

# Podpunkt c
a3 = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
print_info('C', a3)

# Podpunkt d
a4 = np.array([[4, 3, -1], [7, -2, 3], [5, -18, 13]])
print_info('D', a4)