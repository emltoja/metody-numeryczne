# Zadanie 2 Lista 2. Rozkład LU macierzy
import numpy as np


# Korzystamy z twierdzenia Cauchy'ego oraz z faktu, że
# wyznacznik macierzy diagonalnej jest iloczynem
# elementów na jej przkeątnej
def LU_det(L: np.ndarray, U: np.ndarray):
    return L.diagonal().prod() * U.diagonal().prod()


def print_info(subex: str, L: np.ndarray, U: np.ndarray):
    print(f"========PODPUNKT {subex.capitalize()}=========")
    print(f"Wyznacznik macierzy A=L*U: {LU_det(L, U)}")
    print("===========================")


# Podpunkt A

l1 = np.array([[1, 0, 0], [1, 1, 0], [1, 5 / 3, 1]])
u1 = np.array([[1, 2, 4], [0, 3, 21], [0, 0, 0]])

print_info("A", l1, u1)

# Podpunkt B

l2 = np.array([[2, 0, 0], [-1, 1, 0], [1, -3, 1]])
u2 = np.array([[2, -1, 1], [0, 1, -3], [0, 0, 1]])

print_info("B", l2, u2)
