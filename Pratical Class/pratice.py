"""

#runje_kuttta method

def function(x, y):
    return 3*x*x*y

def runje_kutta_method(x0, x, y, h):
    while x0<x:
    
        k1 = function(x0, y)
    
        k2 = function(x0 + h/2, y+(h/2)*k1)
    
        k3 = function(x0 + h/2, y+(h/2)*k2)
    
        k4 = function(x0 + h, y+h*k3)
    
        y = y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
    
        print(f"The value of y at x = {x0:.1f} is {y:.8f}")
        print("")
    
        x0 = x0 + h
    
x0 = 0
y = 1
x = 1
h = 0.1

runje_kutta_method(x0, x, y, h)



import numpy as np

def function(x, y):
    return 3*x*x*y

def exact_solution(x):
    return np.exp(x*x)

def predictor_corrector_method(function, x0, y0, h, x):
    
    n = int((x-x0)/h)
    
    n_value = 0
    
    x = np.linspace(x0, x, n+1)
    y = np.zeros(n+1)
    error = np.zeros(n+1)
    y[0] = y0
    y_exact = np.zeros(n+1)
    
    
    #eulers method
    y[1] = y0 + h*function(x0, y0)
    print(f"The initial conditions are n={n_value}, x = {x[0]}, y = {y[0]}")
    print("")
    
    #predictor-corrector loop
    for i in range(1, n):
        
        y_predictor = y[i] + (h/3)*(3*function(x[i], y[i]) - function(x[i-1], y[i-1]))
        print(f" The value of y at x = {'%.1f'%x[i]} using predictor method is---> {'%.10f'%y_predictor}")
        print(" ")
        
        y_corrector = y[i] + (h/12) * (5*function(x[i+1], y_predictor)) + 8*function(x[i], y[i]) - function(x[i-1], y[i-1])
        y[i+1] = y_corrector
        print(f" The value of y at x = {'%.1f'%x[i]} using corrector method is---> {'%.10f'%y_corrector}")
        print(" ")
        
        y_exact[i+1] = exact_solution(x[i+1])
        error[i+1] = abs(y_exact[i+1] - y[i+1])
        
        n_value += 1
        print(f"The value of n is {n_value}, x = {'%.1f'%x[i]}")
        print(" ")
        
    for i in range(1, n):
        print(f"n = {i}: x = {x[i]:.4f}, y_approx = {y[i]:.6f}, y_exact = {y_exact[i]:.6f}, Error = {error[i]:.6f}")
        
    return x, y

x0 = 0
y0 = 1
h = 0.1
x = 1

x_value, y_value = predictor_corrector_method(function, x0, y0, h, x)




#predictor-corrector method

import numpy as np

def function(x, y):
    return 3*x*x*y

def exact_solution(x):
    np.exp(x**3)

def predictor_corrector_method(function, x0, y0, x_end, h):
    
    n = int((x_end-x0)/h)
    
    n_value = 0
    
    x = np.linspace(x0, x_end, n+1)
    y = np.zeros(n+1)
    error = np.zeros(n+1)
    
    y[0] = y0
    y_exact = np.zeros(n+1)
    
    y[1] = y0 + h* function(x0, y0)
    print(f"The intial conditions are n = {n_value}, x = {x[0]}, y = {y[0]}")
    
    for i in range(2, n):
        
        y_predictor = y[i] + (h/12) * (23*function(x[i], y[i])- 16*function(x[i-1], y[i-1]) + 5*function(x[i-2], y[i-2]))
        print(f"The predictor value of y at n = {i}, x = {x[i]} is {'%.8f'%y_predictor}")
        print("")
        
        y_corrector = y[i] + (h/24) * (9*function(x[i+1], y_predictor) + 19*function(x[i], y[i]) - 5*function(x[i-1], y[i-1]) + function(x[i-2], y[i-2]))
        y[i+1] = y_corrector
        print(f"The corrector value of y at n = {i}, x = {x[i]} is {'%.8f'%y_corrector}")
    
        y_exact[i+1] = exact_solution(x[i+1])
        error[i+1] = abs(y_exact[i+1] - y[i+1])
        
        n_value += 1
        print(f"The value of n is {n_value}, x = {x[i]}")
        print("")
    
    
    for i in range(1, n):
        print(f"n = {i}: x = {x[i]:.4f}, y_approx = {y[i]:.6f}, y_exact = {y_exact[i]:.6f}, Error = {error[i]:.6f}") 
        
    return x, y

x0 = 0
y0 = 1
h = 0.1
x_end = 1

x_value, y_value = predictor_corrector_method(function, x0, y0, x_end, h)

"""

import numpy as np

def function(x, y):
    return 3*x*x*y

def exact_solution(x):
    return np.exp(x**3)

def predictor_corrector_method(function, x0, y0, x_end, h):
    
    n = int((x_end-x0)/h)
    
    n_value = 0
    
    x = np.linspace(x0, x_end, n+1)
    y = np.zeros(n+1)
    error = np.zeros(n+1)
    
    y[0] = y0
    y_exact = np.zeros(n+1)
    
    y[1] = y0 + h* function(x0, y0)
    print(f"The initial conditions are n = {n_value}, x = {x[0]}, y = {y[0]}")
    
    for i in range(2, n):
        
        y_predictor = y[i] + (h/12) * (23*function(x[i], y[i])- 16*function(x[i-1], y[i-1]) + 5*function(x[i-2], y[i-2]))
        print(f"The predictor value of y at n = {i}, x = {x[i]} is {'%.8f'%y_predictor}")
        print("")
        
        y_corrector = y[i] + (h/24) * (9*function(x[i+1], y_predictor) + 19*function(x[i], y[i]) - 5*function(x[i-1], y[i-1]) + function(x[i-2], y[i-2]))
        y[i+1] = y_corrector
        print(f"The corrector value of y at n = {i}, x = {x[i]} is {'%.8f'%y_corrector}")
    
        y_exact[i+1] = exact_solution(x[i+1])
        error[i+1] = abs(y_exact[i+1] - y[i+1])
        
        n_value += 1
        print(f"The value of n is {n_value}, x = {x[i]}")
        print("")
    
    
    for i in range(1, n):
        print(f"n = {i}: x = {x[i]:.4f}, y_approx = {y[i]:.6f}, y_exact = {y_exact[i]:.6f}, Error = {error[i]:.6f}") 
        
    return x, y

x0 = 0
y0 = 1
h = 0.1
x_end = 1

x_value, y_value = predictor_corrector_method(function, x0, y0, x_end, h)
         
          
        
        
        