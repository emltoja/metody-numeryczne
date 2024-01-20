# Lista 6 Zadanie 1. Całkowanie metodą trapezów 

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-darkgrid')

# Całkowanie metodą trapezów 
def integrate(xs, ys, lower, upper):
    
    start = np.searchsorted(xs, lower)
    end = np.searchsorted(xs, upper)
    deltas = np.diff(xs[start:end]) / 2
    areas = (ys[start:end-1] + ys[start+1:end]) * deltas / 2

    return np.sum(areas)


vs = np.array([1.0, 1.8, 2.4, 3.5, 4.4, 5.1, 6.0])
Ps = np.array([4.7, 12.2, 19.0, 31.8, 40.1, 43.8, 43.2])
mass = 2000

integral = integrate(vs, vs[1:] / Ps[1:], 1, 6)
print("Całka z v/P = ", integral)  
print(f"Delta t = {mass * integral}")


plt.plot(vs, vs / Ps)
plt.plot(vs, vs / Ps, 'ro')
plt.xlabel("v [m/s]")
plt.ylabel("v/P")

plt.title("Wykres v/P(v) z aproksymowaną całką")
plt.gcf().set_size_inches(12, 6)

# Plot trapezoids under the curve
for i in range(len(vs) - 1):
    plt.fill_between([vs[i], vs[i+1]], [vs[i] / Ps[i], vs[i+1] / Ps[i+1]], color='orange', edgecolor='red', alpha=0.3)

plt.show()