# Interpolacja wielomianowa

import numpy as np
import matplotlib.pyplot as plt


def interpolate(xs, ys):

    n = len(xs)
    A = np.zeros((n, n))
    for i in range(n):
        A[i, 0] = 1
        for j in range(1, n):
            A[i, j] = A[i, j - 1] * xs[i]

    return np.linalg.solve(A, ys)

def polyval(coefs, x):
    return sum([coefs[i] * x ** i for i in range(len(coefs))])


xs = np.array([0.2, 2, 20, 200, 2000, 20_000])
ys = np.array([103, 13.9, 2.72, 0.8, 0.401, 0.433])


coeffs = interpolate(xs, ys)
xrange = np.linspace(0.2, 20_000, 100000)
yrange = polyval(coeffs, xrange)
xzoom = np.linspace(0.2, 200, 1000)
yzoom = polyval(coeffs, xzoom)

print(f"Współczynnik oporu dla Re=5    : {polyval(coeffs, 5):.3f}")
print(f"Współczynnik oporu dla Re=50   : {polyval(coeffs, 50):.3f}")
print(f"Współczynnik oporu dla Re=5000 : {polyval(coeffs, 5000):.3f}")

fig, ax = plt.subplots(1, 2)
fig.set_size_inches(12, 6)
ax[0].plot(xs, ys, 'o')
ax[0].plot(xrange, yrange)
ax[0].grid()
ax[0].set_title('Interpolacja wielomianowa')
ax[1].plot(xs[:4], ys[:4], 'o')
ax[1].plot(xzoom, yzoom)
ax[1].set_title('Interpolacja wielomianowa (zoom)')
ax[1].grid()
plt.show()