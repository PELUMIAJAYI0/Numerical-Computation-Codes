import numpy as np

def function(x, y):
    return 3*x*x*y

def predictor_corrector_method(function, x0, y0, h, x):
    
    n = int((x-x0)/h)
    
    n_value = 0
    
    x = np.linspace(x0, x, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    
    #eulers method
    #when n =0
    y[1] = y0 + h*function(x0, y0)
    print(f"The initial conditions are n={n_value}, x = {x[n_value]}, y = {y[n_value]}")
    print("")
    
    #predictor-corrector loop
    
    for i in range(1, n):
        
        y_predictor = y[i] + (h/2)*(3*function(x[i], y[i]) - function(x[i-1], y[i-1]))
        print(f" The value of y at x = {'%.1f'%x[i]} using predictor method is---> {'%.10f'%y_predictor}")
        print(" ")
        
        y_corrector = y[i] + (h/12) * (5*function(x[i+1], y_predictor) + 8*function(x[i], y[i]) - function(x[i-1], y[i-1]))
        y[i+1] = y_corrector
        print(f" The value of y at x = {'%.1f'%x[i]} using corrector method is---> {'%.10f'%y_corrector}")
        print(" ")
        
        n_value += 1
        print(f"The value of n is {n_value}, x = {x[n_value]}, y = {y[n_value]}")
        print(" ")
        
    return x, y


x0 = 0
y0 = 1
h = 0.1
x = 1

x_value, y_value = predictor_corrector_method(function, x0, y0, h, x)