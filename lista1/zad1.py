# Lista 1 Zadanie 1
import matplotlib.pyplot as plt
import numpy as np
import sys


# Pierwsza wersja przbliżenia Padego funkcji exp(-x)
def z1(x):
    return (6 - 2 * x) / (6 + 4 * x + x**2)


# Wersja druga
def z2(x):
    return (6 - 4 * x + x**2) / (6 + 2 * x)


def main():
    xs = np.linspace(0, 3, 100)

    first_aproximation = z1(xs)
    second_aproximation = z2(xs)

    exact_values = np.exp(-1 * xs)

    plt.style.use("seaborn-v0_8-dark")

    fig, ax = plt.subplots()
    ax.plot(xs, first_aproximation, label="z1")
    ax.plot(xs, second_aproximation, label="z2")
    ax.plot(xs, exact_values, label="exp(-x)")
    ax.legend()
    ax.set_title("Przybliżenia Padego")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid()
    fig.savefig("przyblizenia1.png")

    fig, ax = plt.subplots(2, 1)
    fig.suptitle("Przybliżenia Padego")
    ax[0].plot(xs, first_aproximation, label="z1")
    ax[0].plot(xs, exact_values, label="exp(-x)")
    ax[0].legend()
    ax[1].plot(xs, second_aproximation, label="z2")
    ax[1].plot(xs, exact_values, label="exp(-x)")
    ax[1].legend()

    for a in ax:
        a.set_xlabel("x")
        a.set_ylabel("y")
        a.grid()

    fig.savefig("przybliżenia2.png")

    z1_err = np.abs(first_aproximation - exact_values)
    z2_err = np.abs(second_aproximation - exact_values)

    fig, ax = plt.subplots()
    ax.plot(xs, z1_err, label="z1")
    ax.plot(xs, z2_err, label="z2")
    ax.legend()
    ax.set_title("Błędy bezwzględne przybliżeń")
    ax.grid()
    fig.savefig("bledy_bezwzgledne.png")

    fig, ax = plt.subplots()
    ax.plot(xs, z1_err / exact_values, label="z1")
    ax.plot(xs, z2_err / exact_values, label="z2")
    ax.legend()
    ax.set_title("Błędy względne przybliżeń")
    ax.grid()
    fig.savefig("bledy_wzgledne.png")


if __name__ == "__main__":
    main()
