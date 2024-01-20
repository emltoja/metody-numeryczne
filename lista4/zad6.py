# Zadanie 6 Lista 4. Pierwiastki wielomianów. 

import numpy as np
import numpy.linalg as la


# Metoda z macierzą towarzyszącą 
def roots(p):
    n = len(p) - 1
    A = np.zeros((n, n), dtype=np.complex128)
    A[0, :] = -p[1:] / p[0]
    A[np.arange(1, n), np.arange(n-1)] = 1
    return la.eigvals(A)


# Wartość wielomianu
def evalPoly(a, p):
    return sum([p[i] * a**(len(p) - i - 1) for i in range(len(p))])

p = np.array([1.0 + 0j, 5 + 1j, -8 + 5j, 30 - 14j, -84 + 0j])
rs = roots(p)
print("Pierwiastki wielomianu: ")
for (i, root) in enumerate(rs): 
    print(f"x{i} = {np.round(root, 2)}")
for (i, root) in enumerate(rs):
    s = str(np.round(evalPoly(root, p), 2))
    print(f"Wartość dla pierwiastka: x{i}: {s.rjust(len(s))}")
