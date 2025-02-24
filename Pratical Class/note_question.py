"""
import numpy as np
import matplotlib.pyplot as plt

def predictor_corrector(f, y0, x_range, h):
    x_values = np.arange(x_range[0], x_range[1] + h, h)
    y_values = np.zeros_like(x_values)
    y_values[0] = y0
    
    for i in range(len(x_values) - 1):
        x, y = x_values[i], y_values[i]
        
        # Predictor step (Euler Method)
        y_predict = y + h * f(x, y)
        
        # Corrector step (Trapezoidal Method)
        y_correct = y + (h / 2) * (f(x, y) + f(x + h, y_predict))
        
        # Update y value
        y_values[i + 1] = y_correct
    
    return x_values, y_values

# First ODE: y' = -y, y(0) = 1
def f1(x, y):
    return -y

x_vals1, y_vals1 = predictor_corrector(f1, y0=1, x_range=(0, 1), h=0.001)

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(x_vals1, y_vals1, label="y' = -y", linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title("Predictor-Corrector Method for y= -y")
plt.grid()
plt.show()

"""

import numpy as np
import matplotlib.pyplot as plt

def predictor_corrector(f, y0, x_range, h):
    x_values = np.arange(x_range[0], x_range[1] + h, h)
    y_values = np.zeros_like(x_values)
    y_values[0] = y0
    
    for i in range(len(x_values) - 1):
        x, y = x_values[i], y_values[i]
        
        # Predictor step (Euler Method)
        y_predict = y + h * f(x, y)
        
        # Corrector step (Trapezoidal Method)
        y_correct = y + (h / 2) * (f(x, y) + f(x + h, y_predict))
        
        # Update y value
        y_values[i + 1] = y_correct
    
    return x_values, y_values

# Second ODE: y' = -x(y + y^2), y(0) = 1
def f2(x, y):
    return -x * (y + y**2)

x_vals2, y_vals2 = predictor_corrector(f2, y0=1, x_range=(0, 1), h=0.001)

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(x_vals2, y_vals2, label="y' = -x(y + y^2)")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title("Predictor-Corrector Method for y' = -x(y + y^2)")
plt.grid()
plt.show()