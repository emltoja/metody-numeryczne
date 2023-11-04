# Błędy działań
import numpy as np
import matplotlib.pyplot as plt

xs = np.arange(1, 51)
ys = xs / 100 * 100 - xs

colors = ["blue" if y == 0 else "red" for y in ys]

fig, ax = plt.subplots()
fig.set_size_inches(12, 6)
ax.set_title("Błędy działań")
ax.set_xlabel("x")
ax.set_ylabel("x / 100 * 100 - x")
ax.set_xticks([x for (i, x) in enumerate(xs) if ys[i] != 0])
ax.set_yticks([y for y in ys if y != 0] + [0])
ax.scatter(xs, ys, color=colors)
ax.grid(linestyle="dashed")
plt.show()
