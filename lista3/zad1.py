# Zadanie 1 Lista 3. Macierz Hilberta.
import sys

sys.path.insert(1, "E:/Studia/sem5/metody_numeryczne/listy/lista2")
from zad4 import gauss
import numpy as np
from numpy import linalg as la


def jacobi(A: np.ndarray, b: np.ndarray, eps: float, max_iter=1000, initial_guess: np.ndarray = None):

    if (np.dot(A, initial_guess) == b).all():
        return (initial_guess, 0)
    # Sprawdzamy czy macierz jest diagonalnie dominująca
    for i in range(len(A)):
        if abs(A[i, i]) < sum(abs(A[i, :])) - abs(A[i, i]):
            print("UWAGA!: Macierz nie jest diagonalnie dominująca")
            break
            
    if initial_guess is None:
        x = np.zeros(len(A))
    else:
        x = initial_guess

    count = 0
    while count < max_iter:
        x_prev = x.copy()
        for i in range(len(A)):
            x[i] = (b[i] - np.dot(A[i, :i], x_prev[:i]) - np.dot(A[i, i + 1 :], x_prev[i + 1 :])) / A[i, i]
        count += 1
        # Jeśli poprzednie rozwiązanie jest dostatecznie blisko obecnego to kończymy
        if la.norm(np.dot(A, x) - b) < eps:
            break
    else:
        print("Rozwiązanie nie jest zbieżne.")
    return (x, count)


if __name__ == "__main__":
    hilbert = np.array([[1 / (i + j - 1) for i in range(1, 6)] for j in range(1, 6)])
    b = np.array(range(5, 0, -1))

    initial_guess = gauss(hilbert, b)
    solution, count = jacobi(hilbert, b, 0.05, initial_guess=initial_guess + 0.001)
    print(f"Ilość iteracji: {count}")
    print(f"Rozwiązanie: {solution}")
    print(f"Ax = {np.dot(hilbert, solution)}")
    print(f"b = {b}")
