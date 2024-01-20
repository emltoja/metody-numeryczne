# Lista 6 Zadanie 4. Okres drgań wahadła 
import numpy as np
import matplotlib.pyplot as plt

def hamp(amp):

    def h(theta):
        return 1 / np.sqrt(1 - np.sin(amp/2)**2 * np.sin(theta)**2)
    
    return h


def integrate(amp, lower, upper, num_knots):

    xs = np.linspace(lower, upper, num_knots)
    ys = hamp(amp)(xs)

    deltas = np.diff(xs)
    areas = (ys[:-1] + ys[1:]) * deltas / 2

    return np.sum(areas)


def period(amp):
    return integrate(np.deg2rad(amp), 0, np.pi/2, 10)


print(f'Wartość dla 0deg: {period(0)}')
print(f'Wartość dla 5deg: {period(5)}')
print(f'Wartość dla 10deg: {period(10)}')
print(f'Wartość dla 15deg: {period(15)}')
print(f'Wartość dla 30deg: {period(30)}')
print(f'Wartość dla 45deg: {period(45)}')

print(f'Wartość realna dla 0: {np.pi/2}')