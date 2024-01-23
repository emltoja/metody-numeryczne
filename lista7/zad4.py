# Lista 7, Zadanie 4. Trajektoria rzutu ukośnego 
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import g 
from methods import runge_kutta_4

CW = 0.35
RHO = 1.2
A = 0.01
M = 0.5

def no_drag(v, angle, timestep):

    vy = v * np.sin(angle)
    vx = v * np.cos(angle)

    xs = []
    ys = [] 
    y = 0
    x = 0

    while not ys or y > 0:
    
        xs.append(x)
        ys.append(y)
        vy -= g * timestep
        x  += vx * timestep
        y  += vy * timestep 

    xs.append(x)
    ys.append(0)
    
    return xs, ys


def drag(v, angle, timestep, A):

    vy_init = v * np.sin(angle)
    vx_init = v * np.cos(angle)

    vx_der = lambda t, v: -1 * np.sign(v) * CW * RHO * A * v**2 / M
    vy_der = lambda t, v: -1 * np.sign(v) * CW * RHO * A * v**2 / M - g

    vy = vy_init
    vx = vx_init 

    xs = []
    ys = []
    x = 0
    y = 0

    while not ys or y > 0: 
        
        xs.append(x)
        ys.append(y)

        # acceleration does not depend on time so we can use (0, timestep)
        # instead of (t, t + timestep)
        vx = runge_kutta_4(vx_der, 0, vx, timestep, timestep) 
        vy = runge_kutta_4(vy_der, 0, vy, timestep, timestep)

        x += vx * timestep
        y += vy * timestep

    xs.append(x)
    ys.append(0)

    return xs, ys

def plot_traj_no_drag(v, angle, timestep):
    
    xs, ys = no_drag(v, angle, timestep) 
    ax = plt.axes()

    ax.plot(xs, ys, "r-")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Trajectory of a ball with no drag')
    plt.grid(True)
    plt.show()

def plot_traj_drag(v, angle, timestep, A):

    xs, ys = drag(v, angle, timestep, A)
    ax = plt.axes()

    ax.plot(xs, ys, "r-")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Trajectory of a ball with drag')
    plt.grid(True)
    plt.show()


def plot_drag_trajectories_for_a(ax: plt.Axes, v, angle, timestep, As):
    for a in As:
        xs, ys = drag(v, angle, timestep, a)
        ax.plot(xs, ys, label=f'A = {a}')
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Drag Trajectories for Different A Values')
    ax.grid(True)
    ax.legend()

def plot_drag_trajectories_for_v(ax: plt.Axes, v, angle, timestep, A):
    for v_val in v:
        xs, ys = drag(v_val, angle, timestep, A)
        ax.plot(xs, ys, label=f'v = {v_val}')
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Drag Trajectories for Different v and A Values')
    ax.grid(True)
    ax.legend()


def plot_drag_trajectories_for_angle(ax: plt.Axes, v, angles, timestep, A):
    for angle in angles:
        xs, ys = drag(v, angle, timestep, A)
        ax.plot(xs, ys, label=f'Angle = {np.round(np.rad2deg(angle))}')
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Drag Trajectories for Different Angle Values')
    ax.grid(True)
    ax.legend()




def plot_both_traj(v, angle, timestep, A):

    no_drag_xs, no_drag_ys = no_drag(v, angle, timestep)
    drag_xs, drag_ys = drag(v, angle, timestep, A)

    ax = plt.axes()

    ax.plot(no_drag_xs, no_drag_ys, 'b-', label="No drag")
    ax.plot(drag_xs, drag_ys, 'r-', label='Drag')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Ball trajectories comparison')
    plt.grid(True)
    plt.legend()




plot_both_traj(10, np.pi/4, 0.01, 0.01)
fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# Plot 1: plot_drag_trajectories_for_a
axs[0].set_title('Drag Trajectories for Different A Values')
plot_drag_trajectories_for_a(axs[0], 10, np.pi/4, 0.01, [0.01, 0.1, 1])

# Plot 2: plot_drag_trajectories_for_v
axs[1].set_title('Drag Trajectories for Different V Values')
plot_drag_trajectories_for_v(axs[1], [10, 20, 30], np.pi/4, 0.01, 0.01)

# Plot 3: plot_drag_trajectories_for_angle
axs[2].set_title('Drag Trajectories for Different Angle Values')
plot_drag_trajectories_for_angle(axs[2], 10, [np.pi/6, np.pi/4, np.pi/3], 0.01, 0.01)

plt.tight_layout()
plt.show()

# plot_drag_trajectories_for_a(10, np.pi/4, 0.01, [0.01, 0.1, 1])
# plot_drag_trajectories_for_v([10, 20, 30], np.pi/4, 0.01, 0.01)
# plot_drag_trajectories_for_angle(10, [np.pi/6, np.pi/4, np.pi/3], 0.01, 0.01)