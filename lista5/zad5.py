# Aproksymacja wielomianem stopnia 3

import numpy as np
import matplotlib.pyplot as plt


def cubicfit(xs, ys):

    A = [
            [np.mean(xs ** 6), np.mean(xs ** 5), np.mean(xs ** 4), np.mean(xs ** 3)],
            [np.mean(xs ** 5), np.mean(xs ** 4), np.mean(xs ** 3), np.mean(xs ** 2)],
            [np.mean(xs ** 4), np.mean(xs ** 3), np.mean(xs ** 2), np.mean(xs)],
            [np.mean(xs ** 3), np.mean(xs ** 2), np.mean(xs),      1]
        ]
    

    b = [np.mean(xs ** 3 * ys), np.mean(xs ** 2 * ys), np.mean(xs * ys), np.mean(ys)]

    coeffs = np.linalg.solve(A, b)


    return coeffs


xs = np.array([0, 21.1, 37.8, 54.4, 71.1, 87.8, 100])
ys = np.array([1.79, 1.13, 0.696, 0.519, 0.338, 0.321, 0.296])

coeffs = cubicfit(xs, ys)

xrange = np.linspace(0, 100, 100)

ts = [10, 30, 60, 90]

for t in ts:
    print(f"Kinematyczna lepkośc wody dla temperatury T={t}: {coeffs[0] * t ** 3 + coeffs[1] * t ** 2 + coeffs[2] * t + coeffs[3]}")

plt.plot(xs, ys, 'o')
plt.plot(xrange, coeffs[0] * xrange ** 3 + coeffs[1] * xrange ** 2 + coeffs[2] * xrange + coeffs[3])
plt.title('Aproksymacja wielomianem stopnia 3')
plt.gcf().set_size_inches(12, 6)
plt.grid()
plt.show()
