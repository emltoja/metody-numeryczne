import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt


def F(x):
    return np.array([np.tan(x[0]) - x[1] - 1, np.cos(x[0]) - 3*np.sin(x[1])])

def J(x): 
    return np.array([[1/(np.cos(x[0])**2), -1], [-np.sin(x[0]), -3*np.cos(x[1])]])


def newton(F, J, start, eps, max_iter):

    x = start
    for count in range(max_iter):

        if la.norm(F(x)) <= eps:
            return count, x
        
        x = np.subtract(x, np.dot(la.inv(J(x)), F(x)))
    
    return max_iter, x

xs = np.linspace(0, 1.5, 100)
plt.plot(xs, np.cos(xs) - 3 * np.sin(np.tan(xs) - 1), label='cos(x) - 3 * sin(tan(x) - 1)')
plt.plot(xs, np.zeros(len(xs)))
plt.legend()
plt.show()

eps = 1e-5
max_iter = 1000


xs = [0.88, 1.32, 1.43, 1.475, 1.495]
ys = np.tan(xs) - 1

for x, y in zip(xs, ys):
    sol = newton(F, J, np.array([x, y]), eps, max_iter)
    print("==========================================")
    print(f"Rozwiązanie: {sol[1]}")
    print(f"Ilość iteracji: {sol[0]}")
    print(f"Wartość funkcji: {F(np.array(sol[1]))}")
    print("=========================================")

# print(newton(F, J, np.array([1.3, 10]), eps, max_iter))