# Zadanie 1 Lista 3. Macierz Hilberta.
import numpy as np
from numpy import linalg as la
from scipy.linalg import lu_solve
from scipy.linalg import lu_factor

# Metoda iteracyjnego poprawiania rozwiązań
def correction(A: np.ndarray, b:np.ndarray, eps: float, max_iter=1000):
    x = lu_solve(lu_factor(A), b)
    r = b - np.dot(A, x)
    count = 0
    while count < max_iter:
        if la.norm(r) < la.norm(np.dot(A, x)) * eps or la.norm(r) < la.norm(b) * eps:
            break
        dx = lu_solve(lu_factor(A), r)
        x += dx
        r = b - np.dot(A, x)
        count += 1
    return (x, count)


if __name__ == "__main__":
    hilbert = np.array(
        [[1 / (i + j - 1) for i in range(1, 6)] for j in range(1, 6)], 
        dtype=np.float32
    )
    b = np.array(range(5, 0, -1), dtype=np.float32)

    # Rozwiązanie metodą iteracyjnego poprawiania rozwiązań
    solution, count = correction(hilbert, b, 1e-1)
    print(f"Ilość iteracji: {count}")
    print(f"Rozwiązanie: {solution}")
    print(f"Ax = {np.dot(hilbert, solution)}")
    print(f"b = {b}")
