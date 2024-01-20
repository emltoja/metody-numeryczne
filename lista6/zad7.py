import numpy as np

def diffapx(N, points):
    l = max(points)
    L = int(np.abs(points[0] - points[1])) + 1

    if L < N + 1:
        raise ValueError('More points needed!')

    A = np.zeros((L, L))
    for n in range(L):
        A[0, n] = 1
        for m in range(1, L):
            A[m, n] = A[m - 1, n] * l / m
        l -= 1

    b = np.zeros(L)
    b[N] = 1

    c = np.linalg.solve(A[:L, :], b).T

    err = np.dot(A[L-1, :], c.T)
    eoh = L - N

    if np.abs(err) < np.finfo(float).eps:
        err = np.dot(A[L - 1, :], c.T)
        eoh = L - N + 1

    if points[1] < points[0]:
        c = np.flip(c)  # Flip the coefficients if points are in decreasing order

    return c, err, eoh, A, b # Return coefficients, error, order of error, matrix A and vector b


coefs, err, eoh, A, b = diffapx(1, [2, -2])
print(f"Współczynniki: {coefs}")
print(f"Błąd: {err}")
print(f"Rząd błędu: {eoh}")
print(f"Macierz A: \n{A}")
print(f"Wektor b: {b}")

xs = np.array([0, 0.1, 0.2, 0.3, 0.4])
ys = np.array([0, 0.078348, 0.13891, 0.192916, 0.244981])
step = 0.1 

derivative = np.dot(coefs, ys) / step ** 2

print(f"Pochodna w punkcie 0.2: {derivative}")