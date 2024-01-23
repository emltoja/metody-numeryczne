
# Metoda Eulera 
def euler_method(derivative, init_arg, init_val, target_arg, timestep): 

    x = init_arg 
    y = init_val 

    while x < target_arg:
        y += timestep * derivative(x, y)
        x += timestep 

    return y


# Metoda Rungego-Kutty 2 rzędu
def runge_kutta_2(derivative, init_arg, init_val, target_arg, timestep): 

    x = init_arg 
    y = init_val 

    while x < target_arg: 
        k1 = timestep * derivative(x, y)
        k2 = timestep * derivative(x + timestep, y + k1)
        y += (k1 + k2) / 2
        x += timestep 

    return y


# Metoda Rungego-Kutty 4 rzędu 
def runge_kutta_4(derivative, init_arg, init_val, target_arg, timestep): 

    x = init_arg 
    y = init_val 

    while x < target_arg: 
        k1 = timestep * derivative(x, y)
        k2 = timestep * derivative(x + timestep/2, y + k1/2)
        k3 = timestep * derivative(x + timestep/2, y + k2/2)
        k4 = timestep * derivative(x + timestep, y + k3)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        x += timestep 

    return y