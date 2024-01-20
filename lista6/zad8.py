# Lista 6 Zadanie 8. Różniczkowanie z interpolacją wielominaową. 
import numpy as np 



def interpolate(xs, ys):
    A = np.vander(xs, increasing=True)
    c = np.linalg.solve(A, ys)
    return c 


def derivative(c):
    return np.polyder(c)


xs = np.array([-2.2, -0.3, 0.8, 1.9])
ys = np.array([-15.18, 10.962, 1.92, -2.04])

coefs = interpolate(xs, ys)
print(f"Współczynniki: {coefs}")

der_coefs = derivative(coefs)
print(f'f\'(0) = {np.polyval(der_coefs, 0)}')

der2_coefs = derivative(der_coefs)
print(f'f\'\'(0) = {np.polyval(der2_coefs, 0)}')