# Zadanie 8 Lista 2. Macierz odwrotna
import numpy as np
from numpy import linalg as la


def inverse(A: np.ndarray):
    n = len(A)

    augmented_A = np.hstack((A, np.identity(n)))

    # Przekształcenie macierzy do górnotrójkątnej
    for k in range(n):
        for i in range(k + 1, n):
            factor = augmented_A[i][k] / augmented_A[k][k]
            augmented_A[i, k:] -= factor * augmented_A[k, k:]

    # Przekształcenie macierzy do jednostkowej
    for k in range(n - 1, -1, -1):
        augmented_A[k, :] /= augmented_A[k, k]
        for i in range(k - 1, -1, -1):
            factor = augmented_A[i][k]
            augmented_A[i, :] -= factor * augmented_A[k, :]

    inverse = augmented_A[:, n:]

    return inverse


if __name__ == "__main__":
    a = np.array(
        [
            [2, -1, 0, 0, 0, 0],
            [-1, 2, -1, 0, 0, 0],
            [0, -1, 2, -1, 0, 0],
            [0, 0, -1, 2, -1, 0],
            [0, 0, 0, -1, 2, -1],
            [0, 0, 0, 0, -1, 5],
        ]
    )
    print(f"Macierz odwrotna przy funkcji wbudowanej \n {la.inv(a)} \n")
    print(f"Macierz odwrotna przy funkcji własnej \n {inverse(a)} \n")
