# Aproksymacja funkcją liniową i kwadratową

import numpy as np
import matplotlib.pyplot as plt

def linfit(xs, ys):
    
    beta1 = (np.mean(xs * ys) - np.mean(xs) * np.mean(ys)) / (np.mean(xs ** 2) - np.mean(xs) ** 2)
    beta0 = np.mean(ys) - beta1 * np.mean(xs)

    sse = np.sum((ys - beta0 - beta1 * xs) ** 2)
    sst = np.sum((ys - np.mean(ys)) ** 2)

    r2 = 1 - sse / sst

    return beta0, beta1, sse, sst, r2


def quadfit(xs, ys):
    
    A = [[np.mean(xs ** 4), np.mean(xs ** 3), np.mean(xs ** 2)],
         [np.mean(xs ** 3), np.mean(xs ** 2), np.mean(xs)],
         [np.mean(xs ** 2), np.mean(xs), 1]]
    
    b = [np.mean(xs ** 2 * ys), np.mean(xs * ys), np.mean(ys)]

    coeffs = np.linalg.solve(A, b)
    sse = np.sum((ys - coeffs[0] * xs ** 2 - coeffs[1] * xs - coeffs[2]) ** 2)

    sst = np.sum((ys - np.mean(ys)) ** 2)
    r2 = 1 - sse / sst

    return coeffs, sse, sst, r2



xs = np.array([1.0, 2.5, 3.5, 4.0, 1.1, 1.8, 2.2, 3.7])
ys = np.array([6.008, 15.722, 27.130, 33.772, 5.257, 9.549, 11.098, 28.828])

beta0, beta1, lin_err, ys_err, lin_r2 = linfit(xs, ys)
(a, b, c), quad_err, _, quad_r2 = quadfit(xs, ys)

xrang = np.linspace(1, 4, 100)

print(f'Regresja liniowa:\n y = {beta0:.3f} + {beta1:.3f}x, SSE = {lin_err:.3f}, r2 = {lin_r2:.3f}\n')
print(f'Regresja kwadratowa:\n y = {a:.3f}x^2 + {b:.3f}x + {c:.3f}, SSE = {quad_err:.3f}, r2 = {quad_r2:.3f}\n')


plt.plot(xs, ys, 'o')
plt.plot(xrang, beta0 + beta1 * xrang, label='linfit')
plt.plot(xrang, a * xrang ** 2 + b * xrang + c, label='quadfit')
plt.title('Aproksymacja liniowa i kwadratowa')
plt.gcf().set_size_inches(12, 6)
plt.grid()
plt.legend()
plt.show()
