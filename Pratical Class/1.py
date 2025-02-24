#Ranje kutta method

"""
def function(x, y):
    return 3*x*x*y
    
def runje_jutta(x0, x, y, h):
    while x0 < x:
        k1 = function(x0, y)
    
        xk2 = x0 + 0.1/2
        yk2 = y + 0.1/2 * k1
    
        k2 = function(xk2, yk2) 
    
        yk3 = y + 0.1/2*k2
    
        k3 = function(xk2, yk3)
    
        xk4 = x0 + 0.1
        yk4 = y + 0.1 * k3
    
        k4 = function(xk4, yk4)
    
        y = y + (0.1/6) * (k1+2*k2+2*k3+k4)
        
        x0 = x0+h
    
        print(f"The value of y at x is {'%.1f'%x0} is {'%.8f'%y}")
    
x0 = 0
x = 1
y = 1
h = 0.1

runje_jutta(x0, x, y, h)



import numpy as np
import matplotlib.pyplot as plt

def adams_bashforth_predictor(f, y, t, h, steps):
    """
"""
    Adams-Bashforth Predictor (4th order)
    f: function representing dy/dt = f(t, y)
    y: array of initial values [y0, y1, y2, y3]
    t: array of initial time steps [t0, t1, t2, t3]
    h: step size
    steps: number of steps to predict
    """
"""
    predictions = []
    for i in range(steps):
        # Predict using Adams-Bashforth 4-step method
        y_next = y[-1] + h * (55 * f(t[-1], y[-1]) - 59 * f(t[-2], y[-2]) + 37 * f(t[-3], y[-3]) - 9 * f(t[-4], y[-4])) / 24
        t_next = t[-1] + h
        predictions.append(y_next)
        
        # Update y and t for the next step
        y.append(y_next)
        t.append(t_next)
    
    return predictions

def adams_moulton_corrector(f, y, t, h, steps):
    """
"""    Adams-Moulton Corrector (4th order)
    f: function representing dy/dt = f(t, y)
    y: array of initial values [y0, y1, y2, y3]
    t: array of initial time steps [t0, t1, t2, t3]
    h: step size
    steps: number of steps to correct
    """

"""
    corrections = []
    for i in range(steps):
        # Predict using Adams-Bashforth
        y_pred = y[-1] + h * (55 * f(t[-1], y[-1]) - 59 * f(t[-2], y[-2]) + 37 * f(t[-3], y[-3]) - 9 * f(t[-4], y[-4])) / 24
        t_next = t[-1] + h
        
        # Correct using Adams-Moulton
        y_corr = y[-1] + h * (9 * f(t_next, y_pred) + 19 * f(t[-1], y[-1]) - 5 * f(t[-2], y[-2]) + f(t[-3], y[-3])) / 24
        corrections.append(y_corr)
        
        # Update y and t for the next step
        y.append(y_corr)
        t.append(t_next)
    
    return corrections

# Example ODE: dy/dt = f(t, y)
def f(t, y):
    return -2 * t * y  # Example: dy/dt = -2ty

# Initial conditions
t0 = 0
y0 = 1
h = 0.1  # Step size
steps = 20

# Generate initial values using Euler's method
t = [t0]
y = [y0]

for i in range(3):  # Generate 3 additional initial points
    t_next = t[-1] + h
    y_next = y[-1] + h * f(t[-1], y[-1])
    t.append(t_next)
    y.append(y_next)

# Predict using Adams-Bashforth
predictions = adams_bashforth_predictor(f, y.copy(), t.copy(), h, steps)

# Correct using Adams-Moulton
corrections = adams_moulton_corrector(f, y.copy(), t.copy(), h, steps)

# Print results
print("Predictions (Adams-Bashforth):", predictions)
print("Corrections (Adams-Moulton):", corrections)

# Plot results
plt.plot(t, y, label="Corrected Solution")
plt.xlabel("t")
plt.ylabel("y")
plt.title("Predictor-Corrector Method")
plt.legend()
plt.grid()
plt.show()
        



def function(x, y):
    return 3*x*x*y

def euler(x0, x, y, h):
    while x0 < x:
        
        y = y + 0.1*function(x, y)
        
        
        print(f"The approximate solution of x at {'%.1f'%x} is {'%.8f'%y}")
        
        x0 = x0+h
x0 = 0
x = 1
y = 1
h = 0.1

euler(x0, x, y, h)

def function(x, y):
    return 3*x*x*y

def runje_kutta(x0, x, y, h):
    while x0 < x:
        
        k1 = function(x0, y)
        
        xk2 = x0 + 0.1/2
        yk2 = y + 0.1/2*k1
        
        k2 = function(xk2, yk2)
        
        xk3 = x0 + 0.1/2
        yk3 = y + 0.1/2*k2
        
        k3 = function(xk3, yk3)
        
        xk4 = x0 + 0.1
        yk4 = y + 0.1*k3
        
        k4 = function(xk4, yk4)
        
        y = y + (h/6)* (k1 + 2*k2 + 2*k3 + k4)
        
        x0 = x0 + h
        
        print(f"The approximate solution of x at {'%.1f'%x0} is---> {'%.8f'%y}")
        
        
        
x0 = 0
x = 1
y = 1
h = 0.1

runje_kutta(x0, x, y, h)



import numpy as np
import matplotlib.pyplot as plt

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
        y_predictor = y[i+2] + (h/12) * (23*function(x[i+2], y[i+2]) - 16*function(x[i+1], y[i+1])+ 5*function(x[i], y[i]))
        print(f"The value of y at x = {x[i]} using predictor method is---> {y_predictor}")
        print("")
        
        #y_predictor = y[i+3]
        
        #corrector: Adams Moulton 2-step method
        y_corrector = y[i+2] + (h/24) * (9*function(x[i+3], y_predictor) + 19*function(x[i+2], y[i+2]) - 5*function(x[i+1], y[i+1] + function(x[i], y[i])))
        print(f"The value of y at x = {x[i]} using corrector method is---> {y_corrector}")
        print("")
        
        y[i+3] = y_corrector
        
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



plt.plot(x, y, label = "Adams Bashforth Moulton Method")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Adams Bashforth Moulton Method")
plt.legend()
plt.grid()
plt.show()
"""

#past questions

import numpy as np

def function(x, y):
    return 3*x*x*y

def exact_solution(x, y):
    return np.exp^(x^3)

def adams_bashforth_moulton(x0, y0, h, x_end):
    n = int((x_end-x0)/h)
    
    x = np.linspace(x0, x_end, n+1)
    y = np.zeros(n+1)
    y_exact = np.zeros(n+1)
    error = np.zeros(n+1)
    
    y[0] = y0
    y_exact = y0
    
    print(f"The initial conditions are---> n = 0, x = {x[0]:.4f}, y = {y[0]:.8f}")
    
    
    y[1] = exact_solution(x[1])
    y[2] = exact_solution(x[2])
    
    y_exact[1] = exact_solution(x[1])
    y_exact[2] = exact_solution(x[2])
    
    print(f"n = 1, x = {x[1]:.4f}, y_exact = {y[1]:.6f}")
    print(f"n = 2, x = {x[2]:.4f}, y_exact = {y[2]:.6f}")
    
    for i in range(2, n):
        
        y_predictor = y[i] + (h/12) * (23*function(x[i], y[i])- 16*function(x[i-1], y[i-1]) + 5*function(x[i-2], y[i-2]))
        print(f"The predictor value at when n = {i} is---> {y_predictor}")
        
        y_corrector = y[i] + (h/24) * (9*function(x[i+1], y[i+1]) + 19*function(x[i], y[n]) - 5*function(x[i-1], y[i-1]) + function(x[i-2], y[i-2]))
        print(f"The corrector value at when n = {i} is---> {y_corrector}")

        y[i+1] = y_corrector
        
        y_exact[i+1] = exact_solution(x[i+1])
        error[i+1] = abs(y_exact[i+1]- y[i+1])
        
    print(f"n = {n}, x={x[n]:.4f}, y = {y[n]:.6f}")
    
    print("Comparing with Euler's method")
    for i in range(n+1):
        print(f"n = {i} || x = {x[i]:.4f}, y_approximate = {y[i]:.6f}, y_exact = {y_exact[i]:.6f}, Error = {error[i]:.6f}")
        
    return x,y


x0 = 0
y0 = 1
h = 0.1
x_end = 1

x_value, y_value = adams_bashforth_moulton(x0, y0, h, x_end)