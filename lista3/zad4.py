# Zadanie 4 Lista 3. Norma wektora. 

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt


def generate_B():
    B = np.zeros((20, 20))
    for i in range(20):
        B[i, i] = 0.025 * (i + 1)
        if i != 19:
            B[i, i + 1] = 5

    return B


def calc_norms(n):
    B = generate_B()
    x0 = np.array([1] * 20)
    x = x0
    ratios = np.zeros(n)

    for i in range(1, n):
        new_x = np.dot(B, x)
        ratios[i] = la.norm(new_x, 2) / la.norm(x0, 2)
        x = new_x

    return ratios


def plot_ratios(n):

    ratios = calc_norms(n)
    # Mark the lowest and highest values and give them labels

    plt.annotate(f"max: {np.max(ratios).__round__(3)}", xy=(np.argmax(ratios), np.max(ratios)), xytext=(np.argmax(ratios) + 1, np.max(ratios) + 0.1))
    plt.annotate(f"min: {np.min(ratios).__round__(3)}", xy=(np.argmin(ratios), np.min(ratios)), xytext=(np.argmin(ratios) + 1, np.min(ratios) - 0.1))

    # Mark the points where ratio begins to rise and fall
    for i in range(1, len(ratios) - 1):
        if ratios[i - 1] < ratios[i] and ratios[i] < ratios[i + 1]:
            plt.plot(i, ratios[i], "go")
        elif ratios[i - 1] > ratios[i] and ratios[i] > ratios[i + 1]:
            plt.plot(i, ratios[i], "ro")
        else: 
            plt.plot(i, ratios[i], "bo")

    plt.plot(np.argmin(ratios), np.min(ratios), "bo")
    plt.plot(np.argmax(ratios), np.max(ratios), "bo") 

    plt.xlabel("Iteracja")
    plt.ylabel("Norma")
    plt.grid()
    plt.title("Norma wektora x w funkcji iteracji")
    plt.show()


plot_ratios(100)
    