# Aproksymacja funkcji wykładniczej 

import numpy as np
import matplotlib.pyplot as plt

def expfit(xs, ys):

    transofrmed_ys = np.log(ys)

    xmean = np.mean(xs)
    ymean = np.mean(transofrmed_ys)

    b = np.sum((xs - xmean) * (transofrmed_ys - ymean)) / np.sum((xs - xmean) ** 2)

    loga = ymean - b * xmean

    return np.exp(loga), b


xs = np.array([1.2, 2.8, 4.3, 5.4, 6.8, 7.9])
ys = np.array([7.5, 16.1, 38.9, 67.0, 146.6, 266.2])



a, b = expfit(xs, ys)
sse = np.sum((ys - a * np.exp(b * xs)) ** 2)
std_dev = np.sqrt(sse / (len(xs) - 2))

print(f"y = {a:.3f} * exp({b:.3f} * x)")
print(f"Odchylenie standardowe: {std_dev:.3f}")

xrang = np.linspace(1.2, 7.9, 100) 


plt.plot(xs, ys, 'o')
plt.plot(xrang, a * np.exp(b * xrang))
plt.title('Aproksymacja wykładnicza')
plt.gcf().set_size_inches(12, 6)
plt.grid()
plt.show()

