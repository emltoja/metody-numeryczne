# Zadanie 3 Lista 2. Układ równań LU = b
import numpy as np
from .zad4 import validate


# Rozwiąż układ równań L*U*x = b
def solve_LU(L: np.ndarray, U: np.ndarray, b: np.ndarray):
    assert L.shape == U.shape and U.shape[1] == b.shape[0]

    return solve_right_triangular(U, solve_left_triangular(L, b))


# Rozwiąż układ równań dla macierzy górnotrójkątnej
def solve_right_triangular(U: np.ndarray, b: np.ndarray):
    validate(U, b)
    result = np.zeros(b.shape)
    length = b.shape[0]

    for i in range(length - 1, -1, -1):
        excess = 0
        for j in range(length - 1, i, -1):
            excess += U[i, j] * result[j]
        result[i] = (b[i] - excess) / U[i, i]

    return result


# Rozwiąż układ równań dla macierzy dolnotrójkątnej
def solve_left_triangular(L: np.ndarray, b: np.ndarray):
    validate(L, b)
    result = np.zeros(b.shape)
    length = b.shape[0]

    for i in range(0, length):
        excess = 0
        for j in range(0, i):
            excess += L[i, j] * result[j]
        result[i] = (b[i] - excess) / L[i, i]

    return result

if __name__ == "__main__":
    l = np.array([[1, 0, 0], [1.5, 1, 0], [0.5, 11 / 13, 1]])
    u = np.array([[2, -3, -1], [0, 6.5, -3.5], [0, 0, 32 / 13]])
    b = np.array([1, -1, 2])

    print(solve_LU(l, u, b))
