# Zadanie 2 Lista 3. Metoda Seidla-Gaussa
import sys

sys.path.insert(1, "E:\Studia\sem5\metody_numeryczne\listy")
import numpy as np
import numpy.linalg as la
from lista2.zad3 import solve_left_triangular


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

def dlu(A: np.ndarray): 
    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)

    return (D, L, U)

def gauss_seidel(A: np.ndarray, b: np.ndarray, initial_guess: np.ndarray, eps: float, max_iter: int=1000):
    D, L, U = dlu(A)
    x = initial_guess
    count = 0

    if la.norm(np.identity(len(A)) - np.dot(la.inv(D+L), A)) >= 1:
        raise ValueError("Brak zbieżności")

    while count < max_iter:
        x = solve_left_triangular(D + L, np.dot(-U, x) + b)
        count += 1
        if la.norm(np.dot(A, x) - b) < eps:
            break
        
    return (x, count)


if __name__ == "__main__":

    dim = 10

    a = toeplitz(dim)
    b = np.array([0 for _ in range(dim - 1)] + [100])

    sol, count = gauss_seidel(a, b, np.ones(dim), 1e-3)
    print(f"Ilość iteracji: {count}")
    # Pie wyświetlaj rozwiązania w notacji wykładniczej
    np.set_printoptions(suppress=True)
    print(f"Rozwiązanie: {sol.round(3)}")
    print(f"Ax = {np.dot(a, sol).round(3)}")
    print(f"b = {b}")
