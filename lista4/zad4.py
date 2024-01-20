import warnings
warnings.filterwarnings("ignore")



# Zadanie 4 Lista 4. Energia swobodna Gibbsa. 

import numpy as np
from zad1 import secant

### STAŁE ####
R =  8.3144621 # J/(mol*K)
T0 = 4.44418 # K


def gibbs(t):
    return - R * t * np.log(np.power(t/T0, 5/2))


def solvegibbs(energy, eps=1e-8):
    
    tmax = 1000
    def f(t): return gibbs(t) - energy

    while np.sign(f(0)) == np.sign(f(tmax)):
        tmax *= 2

    return secant(f, 900, tmax, eps, 100)


sol, iter, _ = solvegibbs(-1e5)
print(f"Temperatura dla energii -1e5: {sol}")
print(f"Energia swobodna Gibbsa: {gibbs(sol)}")
print(f"Ilość iteracji: {iter}")









