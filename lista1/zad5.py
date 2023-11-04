import cProfile
import pstats
from pstats import SortKey
import numpy as np

lo = -10
hi = 10
dx = 0.0001


def poly(x):
    return 6 * x**4 + 5 * x**3 - 13 * x**2 + x + 1


def runpoly():
    xs = np.arange(lo, hi, dx)
    poly(xs)


def horner(x):
    return 1 + x * (1 + x * (-13 + x * (5 + 6 * x)))


def runhorner():
    xs = np.arange(lo, hi, dx)
    horner(xs)


print("Wyliczanie postacią ogólną: ")
cProfile.run("runpoly()")
print("Wyliczanie schematem Hornera: ")
cProfile.run("runhorner()")
