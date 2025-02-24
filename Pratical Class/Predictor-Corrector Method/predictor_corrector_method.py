import numpy as np


def function(x, y):
    return 3*x*x*y

def adams_bashforth_moulton(function, x0, y0, h, x):
    n = int((x-x0)/h) #to calculate the number of steps
    
    n_value = 0
    
    
    x = np.linspace(x0, x, n+1) #create an array to store the values of x
    y = np.zeros(n+1) #create an array to store the values of y
    y[0] = y0 #set the first value of y
    
    print(f"The initial conditions are n = 0, x = {x[0]}, y = {y[0]}")
    print("")
    
    
   #euler's method
    y[1] = y0 + h*function(x0, y0)
    print(f"The initial conditions are n = {n_value}, x = {x[1]}, y = {y[1]}")
    print("")
    
    #predictor-corrector loop
    for i in range(1, n):
        
        
        
        #predictor: Adams Bashforth 2-step method
        y_predictor = y[i] + (h/2) * (3*function(x[i], y[i]) - function(x[i-1], y[i-1]))
        print(f"The value of y at x = {x[i]} using predictor method is---> {y_predictor}")
        print("")
        
        #corrector: Adams Moulton 2-step method
        y_corrector = y[i] + (h/12) * (5*function(x[i+1], y_predictor) + 8*function(x[i], y[i]) - function(x[i-1], y[i-1]))
        print(f"The value of y at x = {x[i]} using corrector method is---> {y_corrector}")
        print("")
        
        y[i+1] = y_corrector
        
        print("")
        
        n_value += 1
        print(f"The value of n is---> {n_value}")
        print("")

    return x, y
        
        
    
x0 = 0
y0 = 1
h = 0.1
x = 1

x, y = adams_bashforth_moulton(function, x0, y0, h, x)

