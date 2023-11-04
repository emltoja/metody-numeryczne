# Zadanie 2 Lista 3. Metoda Seidla-Gaussa
import numpy as np
from numpy import linalg as la

# Funkcja generująca macierz Toeplitza z polecenia wymiaru n
def toeplitz(n):
    A = np.zeros((n, n))
    for i in range(n):
        A[i, i] = 4
        if i != 0:
            A[i, i - 1] = -1
        if i != n - 1:
            A[i, i + 1] = -1
    A[n-1, 0] = 1
    A[0, n-1] = 1
    return A

# Implementacja metody Gaussa-Seidla 
def gauss_seidel(A: np.ndarray, b: np.ndarray, eps: float, max_iter=1000, initial_guess: np.ndarray = None):

    # Sprawdzamy czy macierz jest diagonalnie dominująca
    for i in range(len(A)):
        if abs(A[i, i]) < sum(abs(A[i, :])) - abs(A[i, i]):
            print("UWAGA!: Macierz nie jest diagonalnie dominująca")
            break
            
    # Jeśli nie podamy punktu startowego to przyjmujemy wektor zerowy
    if initial_guess is None:
        x = np.zeros(len(A))
    else:
        x = initial_guess

    # Jeśli punkt startowy jest rozwiązaniem to kończymy
    if (np.dot(A, x) == b).all():
        return (x, 0)

    count = 0
    while count < max_iter:
        x_prev = x.copy()
        for i in range(len(A)):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1 :], x_prev[i + 1 :])) / A[i, i]
        count += 1
        # Jeśli rozwiązanie jest dostatecznie dokładne to kończymy
        if la.norm(np.dot(A, x) - b) < eps:
            break
    else:
        print("Rozwiązanie nie jest zbieżne.")
    return (x, count)


if __name__ == "__main__":

    a = toeplitz(20)
    b = np.array([0 for i in range(19)] + [100])

    sol, count = gauss_seidel(a, b, 0.0001)
    print(f"Ilość iteracji: {count}")
    # Print the solution in non scientific notation 
    np.set_printoptions(suppress=True)
    print(f"Rozwiązanie: {sol.round(3)}")
    print(f"Ax = {np.dot(a, sol).round(3)}")
    print(f"b = {b}")
