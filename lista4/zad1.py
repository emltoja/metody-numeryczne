# Zadanie 1 Lista 4. Metody iteracyjne dla układów nieliniowych 
# Autor: Emil Olszewski
# Data: 04.11.2023r. 

import numpy as np
from types import FunctionType

def f(x):
    return np.tan(np.pi - x) - x

def fprime(x):
    return -1 / (np.cos(np.pi - x) ** 2) - 1



# Metoda bisekcji 
def bisection(f: FunctionType, a: float, b: float, eps: float, max_iter: int, fflops: int = 1):
    c = 0
    for count in range(max_iter):
        diff = (b - a) / 2
        c = a + diff # Lepsze niż (a + b) / 2 w arytmetyce zmiennoprzecinkowej
        if np.abs(f(c)) < eps:
            return c, count, (3 + fflops) * count + 2 * fflops * (count - 1)
        if np.sign(f(c)) == np.sign(f(a)):
            a = c
        else:
            b = c
    return c, max_iter, 3 * (fflops + 1) * max_iter


# Metoda Brenth'a
def brent(f: FunctionType, a: float, b:float, eps: float, max_iter: int, fflops: int = 1):

    x = 0    
    for count in range(max_iter): 
        # Bisekcja 
        fa = f(a)
        fb = f(b)
        diff = (b - a) / 2

        c = a + diff
        fc = f(c)
        
        # Odwrotna interpolacja kwadratowa
        fabdiff = fa - fb
        fcadiff = fc - fa
        fbcdiff = fb - fc 

        x = - (a * fb * fc * fbcdiff + b * fa * fc * fcadiff + c * fa * fb * fabdiff) /  \
              (fabdiff * fcadiff * fbcdiff)

        if np.abs(f(x)) < eps:
            return x, count, (23 + 3*fflops) * count

        if (np.sign(fc) != np.sign(fa) and a <= x <= c):
            b = x
        elif (np.sign(fc) != np.sign(fb) and c <= x <= b):
            a = x
        else:
            if np.sign(fa) == np.sign(fc):
                a = c
            else:
                b = c
        
    return x, max_iter, (20 + 3*fflops) * max_iter 


# Metoda siecznych 
def secant(f: FunctionType, a: float, b: float, eps: float, max_iter: int, fflops: int = 1):
    
    c = 0
    for count in range(max_iter):
        fb = f(b)
        c = b - fb * (b - a) / (fb - f(a))
        fc = f(c)
        if np.abs(fc) < eps:
            return c, count, 6 * count
        if np.sign(fc) == np.sign(fb):
            b = c
        else: 
            a = c
    return c, max_iter, (5 + 3 * fflops) * max_iter



# Metoda Newtona
def newton(
        f: FunctionType,
        fprime: FunctionType,
        x0: float,
        eps: float,
        max_iter: int,
        fflops: int = 1,
        fprimeflops: int = 1,
        printxs: bool = False
):
    x1 = 0
    for count in range(max_iter):
        x1 = x0 - f(x0) / fprime(x0)
        if printxs:
            print(f"x{count}: {x1}")
        if np.abs(x1 - x0) < eps:
            return x1, count, (3 + fflops + fprimeflops) * count
        x0 = x1
    return x1, max_iter, (3 + fflops + fprimeflops) * max_iter


if __name__ == "__main__":
    bi_sol, bi_count, bi_flops = bisection(f, -1, 1.1, 1e-16, 1000, 3)
    print(f"Rozwiązanie metodą bisekcji: {bi_sol}")
    print(f"Ilość iteracji: {bi_count}")
    print(f"Ilość flops: {bi_flops}")
    print("=============================================")

    br_sol, br_count, br_flops = brent(f, -1, 1.1, 1e-16, 1000, 3)
    print(f"Rozwiązanie metodą brent'a: {br_sol}")
    print(f"Ilość iteracji: {br_count}")
    print(f"Ilość flops: {br_flops}")
    print("=============================================")

    se_sol, se_count, se_flops = secant(f, -1, 1.1, 1e-16, 1000, 3)
    print(f"Rozwiązanie metodą siecznych: {se_sol}")
    print(f"Ilość iteracji: {se_count}")
    print(f"Ilość flops: {se_flops}")
    print("=============================================")

    ne_sol, ne_count, ne_flops = newton(f, fprime, 1.1, 1e-16, 1000, 3, 5)
    print(f"Rozwiązanie metodą newtona: {ne_sol}")
    print(f"Ilość iteracji: {ne_count}")
    print(f"Ilość flops: {ne_flops}")
    print("=============================================")

