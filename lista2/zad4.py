# Zadanie 4 Lista 2. Układ równań Ax = b
import numpy as np
from numpy import linalg as la


# Poprzestawiaj wiersze tak, aby na głównej diagonali nie było zer
def validate(A: np.ndarray, b: np.ndarray):
    n = b.shape[0]
    for i in range(0, n - 1):
        if A[i, i] != 0:
            continue
        for j in range(i + 1, n):
            if A[j, i] != 0:  # Zamień rzędy
                A[i, :] += A[j, :]
                A[j, :] = A[i, :] - A[j, :]
                A[i, :] -= A[j, :]

                b[i] += b[j]
                b[j] = b[i] - b[j]
                b[i] -= b[j]
                break


# Rozwiąż układ równań Ax = b
def gauss(A: np.ndarray, b: np.ndarray):
    assert A.shape[1] == b.shape[0]
    n = b.shape[0]
    A = A.astype("float64")
    b = b.astype("float64")

    validate(A, b)

    # Przekształcamy macierz w macierz górnotrójkątną
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            if A[i, k] != 0.0:
                lam = A[i, k] / A[k, k]
                A[i, k + 1 : n] -= lam * A[k, k + 1 : n]
                b[i] -= lam * b[k]

    # Wstawianie wstecz
    for k in range(n - 1, -1, -1):
        b[k] = (b[k] - np.dot(A[k, k + 1 : n], b[k + 1 : n])) / A[k, k]
    return b


if __name__ == "__main__":
    a = np.array(
        [
            [0, 0, 2, 1, 2],
            [0, 1, 0, 2, -1],
            [1, 2, 0, -2, 0],
            [0, 0, 0, -1, 1],
            [0, 1, -1, 1, -1],
        ]
    )

    b = np.array([1, 1, -4, -2, -1])

    print(f" Wyznacznik macierzy a: {la.det(a)}")
    print(f" Współczynnik uwarunkowania macierzy a: {la.cond(a)}")
    print(f" Rozwiązanie uzyskane własną implementacją a: {gauss(a, b)}")
    print(f" Rozwiązanie uzyskane funkcją z modułu numpy: {la.solve(a, b)}")
