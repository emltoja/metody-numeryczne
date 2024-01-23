import numpy as np
from methods import runge_kutta_4
import matplotlib.pyplot as plt
# Lista 7, Zadanie 5. Zagadnienia brzegowe ``

inital_arg = 0
initial_y = 0
final_arg = np.pi / 2
final_y = 1
timestep = 0.1

# Define the boundary value problem and initial conditions
def v_der(x, y):
    return (0.2*x - 1) * y**2 

def shooting_method(initial_arg, initial_y, final_arg, final_y, timestep, init_v_guess):

    v = init_v_guess
    y = initial_y
    x = initial_arg

    while x < final_arg:
        v= runge_kutta_4(v_der, x, v, x + timestep, timestep)
        x += timestep
        y += v * timestep

    return y - final_y

def find_initial_v(initial_arg, initial_y, final_arg, final_y, timestep, init_v_guess1, init_v_guess2):

    v1 = init_v_guess1
    v2 = init_v_guess2

    while abs(v1 - v2) > 1e-5:
        v_mid = (v1 + v2) / 2
        v1_err = shooting_method(initial_arg, initial_y, final_arg, final_y, timestep, init_v_guess1)
        v2_err = shooting_method(initial_arg, initial_y, final_arg, final_y, timestep, init_v_guess2)
        mid_err = shooting_method(initial_arg, initial_y, final_arg, final_y, timestep, v_mid)
        if mid_err * v2_err < 0:
            v1 = v_mid
        elif mid_err * v1_err < 0:
            v2 = v_mid
        else: 
            raise ValueError("Initial guesses do not bracket the solution")

    return v_mid


def solve(initial_arg, initial_y, final_arg, final_y, timestep): 

    v = find_initial_v(initial_arg, initial_y, final_arg, final_y, timestep, 0.5, 3)
    y = initial_y
    x = initial_arg

    xs = [x]
    ys = [y]
    while x < final_arg:
        v = runge_kutta_4(v_der, x, v, x + timestep, timestep)
        x += timestep
        y += v * timestep
        xs.append(x)
        ys.append(y)

    return xs, ys 

xs, ys = solve(inital_arg, initial_y, final_arg, final_y, timestep)
plt.plot(xs, ys)
# plot boundary conditions
plt.plot([inital_arg, final_arg], [initial_y, final_y], 'ro')
plt.show()