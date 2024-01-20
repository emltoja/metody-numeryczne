
# Zadanie 1, Lista 5. Interpolacja kwadratowa.  
import numpy as np
import matplotlib.pyplot as plt

def interpolate(xs, ys):
    
    """Interpolacja kwadratowa.
    :param xs: lista argumentów
    :param ys: lista wartości
    :return: [a, b, c] t. że f(x) = ax^2 + bx + c
    """
    n = len(xs)
    A = np.zeros((n, n))
    for i in range(n):
        A[i, 0] = 1
        for j in range(1, n):
            A[i, j] = A[i, j - 1] * xs[i]
    return np.linalg.solve(A, ys)


xs = [0, 3, 6]
ys = [1.225, 0.905, 0.652]

coeffs = interpolate(xs, ys)
xrange =  np.linspace(0, 6, 100)
yrange = [coeffs[2] * x ** 2 + coeffs[1] * x + coeffs[0] for x in xrange]

print(f"y = {coeffs[2]:.3f}x^2 + {coeffs[1]:.3f}x + {coeffs[0]:.3f}")

plt.plot(xs, ys, 'o')
plt.plot(xrange, yrange)
plt.title('Interpolacja kwadratowa')
plt.gcf().set_size_inches(12, 6)
plt.grid()
plt.show()

