# Zadanie 5 Lista 2. Współczynniki wielomianu
import numpy as np
from zad4 import gauss


def poly(x):
    return np.array([1, x, x**2, x**3, x**4])


a = np.array([poly(0), poly(1), poly(3), poly(5), poly(6)])
b = np.array([-1, 1, 3, 2, -2])

solution = gauss(a, b)


def check_solution(sol):
    def poly_value(x):
        return np.dot(sol, poly(x))

    print(f"Rozwiązanie {sol}")
    print(f"Oczekiwane wartości wielomianu: -1, 1, 3, 2, -2")
    print(f"Otrzymane wartości wielomianu: {[poly_value(x) for x in (0, 1, 3, 5, 6)]}")


check_solution(solution)
