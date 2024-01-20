import sys

sys.path.insert(1, "E:/Studia/sem5/metody_numeryczne/listy/")

from lista2.zad4 import gauss
from zad2 import toeplitz, gauss_seidel
import numpy as np
import timeit
import cProfile

a = toeplitz(10)
b = np.array([0 for _ in range(9)] + [100])


def benchmark():

    sol, count = gauss_seidel(a, b, np.zeros(10), 1e-3)
    print(f"Ilość iteracji: {count}")
    # Nie wyświetlaj rozwiązania w notacji naukowej
    np.set_printoptions(suppress=True)
    print(f"Rozwiązanie: {sol.round(3)}")
    print(f"Ax = {np.dot(a, sol).round(3)}")
    print(f"b  = {b}")
    
    print("\n\nBenchmarking Gauss-Seidel method versus Gauss elimination the numpy.linalg.solve function using cProfile.")
    print("=============================================================================================================")
    print("\n")
    cProfile.run('gauss_seidel(a, b, np.zeros(10), 0.0001)')
    print("\n")
    cProfile.run('np.linalg.solve(a, b)')
    print("\n")
    cProfile.run('gauss(a, b)')
    print("\n")
    print("Benchmarking Gauss-Seidel method vs Gauss elimination vs the numpy.linalg.solve function using timeit.")
    print("======================================================================================================")
    print("\n")
    print("The Gauss-Seidel method took:", end=" ")
    print(timeit.timeit("gauss_seidel(a, b, np.zeros(10), 0.0001)", number=1000, globals=globals()).__round__(3), end=" ")
    print("seconds")
    print("\n")
    print("The numpy.linalg.solve function took:", end=" ")
    print(timeit.timeit("np.linalg.solve(a, b)", number=1000, globals=globals()).__round__(3), end=" ")
    print("seconds")
    print("\n")
    print("The Guass elimination method took:", end=" ")
    print(timeit.timeit("gauss(a, b)", number=1000, globals=globals()).__round__(3), end=" ")
    print("seconds")


benchmark()
