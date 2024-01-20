# Zadnie 2 Lista 5. Interpolacja funkcjami sklejanymi.

import numpy as np
import scipy.interpolate as fit
import matplotlib.pyplot as plt

def interpolate(xs, ys):
    
    cubicfit = fit.CubicSpline(xs, ys, bc_type='natural')

    return cubicfit


xs = np.array([0.2, 2, 20, 200, 2000, 20_000])
ys = np.array([103, 13.9, 2.72, 0.8, 0.401, 0.433])

cubicfit = interpolate(xs, ys)

xrange = np.linspace(0.2, 20_000, 10000)
xzoom = np.linspace(0.2, 200, 1000)

print(f"Współczynnik oporu dla Re=5    : {cubicfit(5):.3f}")
print(f"Współczynnik oporu dla Re=50   : {cubicfit(50):.3f}")
print(f"Współczynnik oporu dla Re=5000 : {cubicfit(5000):.3f}")

fig, ax = plt.subplots(1, 2)
fig.set_size_inches(12, 6)

ax[0].plot(xs, ys, 'o')
ax[0].plot(xrange, cubicfit(xrange))
ax[0].set_title('Interpolacja funkcjami sklejanymi')
ax[0].grid()

ax[1].plot(xs[:4], ys[:4], 'o')
ax[1].plot(xzoom, cubicfit(xzoom))
ax[1].set_title('Interpolacja funkcjami sklejanymi (zoom)')
ax[1].grid()


plt.show()
