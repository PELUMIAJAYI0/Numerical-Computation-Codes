"""

import numpy as np


def function(x, y):
    return 3*x*x*y

def exact_solution(x):
    return np.exp(x**3)  # y = e^(x^3)

def adams_bashforth_moulton(function, x0, y0, h, x_end):
    """
"""
    Three-Step Adams-Bashforth Predictor and Adams-Moulton Corrector
    """
"""
    # Number of steps
    n = int((x_end - x0) / h)
    
    # Initialize arrays
    x = np.linspace(x0, x_end, n+1)  # Create x values
    y = np.zeros(n+1)  # Store y values
    y[0] = y0  # Initial condition
    
    print(f"The initial conditions are---> n = 0: x = {x[0]:.4f}, y = {y[0]:.6f}")
    print("")
    
    # Use exact solution to compute y1 and y2
    y[1] = exact_solution(x[1])
    y[2] = exact_solution(x[2])
    
    print("The results using exact solution are--> ")
    print(f"-------------------------------------------")
    print(f"n = 1: x = {x[1]:.4f}, y_exact = {y[1]:.6f}")
    print(f"n = 2: x = {x[2]:.4f}, y_exact = {y[2]:.6f}")
    print(f"-------------------------------------------")
    print("")

    # Predictor-Corrector loop starts from i = 2
    for i in range(2, n-2):  # n-2 because we need y[i+3]
        
        # Predictor: Adams-Bashforth 3-step method
        y_predictor = y[i+2] + (h/12) * (23*function(x[i+2], y[i+2]) - 16*function(x[i+1], y[i+1]) + 5*function(x[i], y[i]))
        print(f"n = {i}: Predictor y_pred = {y_predictor:.6f}")
        
        # Corrector: Adams-Moulton 3-step method
        y_corrector = y[i+2] + (h/24) * (9*function(x[i+3], y_predictor) + 19*function(x[i+2], y[i+2]) - 5*function(x[i+1], y[i+1]) - function(x[i], y[i]))
        print(f"n = {i}: Corrector y_corrected = {y_corrector:.6f}")

        # Store the corrected value
        y[i+3] = y_corrector
        
    # Print final result
    print(f"n = {n}: x = {x[n]:.4f}, y = {y[n]:.6f}")

    return x, y


# Example usage
x0 = 0
y0 = 1
h = 0.1
x_end = 1

x_vals, y_vals = adams_bashforth_moulton(function, x0, y0, h, x_end)
"""

import numpy as np

def function(x, y):
    return 3*x*x*y  # Given differential equation: y' = 3x²y

def exact_solution(x):
    return np.exp(x**3)  # Given exact solution: y = e^(x³)

def adams_bashforth_moulton(function, x0, y0, h, x_end):
    """
    Three-Step Adams-Bashforth Predictor and Adams-Moulton Corrector
    """
    # Number of steps
    n = int((x_end - x0) / h)
    
    # Initialize arrays
    x = np.linspace(x0, x_end, n+1)  # Create x values
    y = np.zeros(n+1)  # Store y values
    y_exact = np.zeros(n+1)  # Store exact values
    error = np.zeros(n+1)  # Store errors
    
    y[0] = y0  # Initial condition
    y_exact[0] = y0  # Exact solution at x0

    print(f"\nThe initial conditions are---> n = 0: x = {x[0]:.4f}, y = {y[0]:.6f}")

    # Use exact solution to compute y1 and y2
    y[1] = exact_solution(x[1])
    y[2] = exact_solution(x[2])
    
    y_exact[1] = exact_solution(x[1])
    y_exact[2] = exact_solution(x[2])

    print("\nThe results using exact solution are--> ")
    print("-------------------------------------------")
    print(f"n = 1: x = {x[1]:.4f}, y_exact = {y[1]:.6f}")
    print(f"n = 2: x = {x[2]:.4f}, y_exact = {y[2]:.6f}")
    print("-------------------------------------------\n")

    # Predictor-Corrector loop starts from i = 2
    for i in range(2, n):  # Fix the loop range
        
        # Predictor: Adams-Bashforth 3-step method
        y_pred = y[i] + (h/12) * (23*function(x[i], y[i]) - 16*function(x[i-1], y[i-1]) + 5*function(x[i-2], y[i-2]))
        print(f"n = {i}: Predictor y_pred = {y_pred:.6f}")
        
        # Corrector: Adams-Moulton 3-step method
        y_corr = y[i] + (h/24) * (9*function(x[i+1], y_pred) + 19*function(x[i], y[i]) - 5*function(x[i-1], y[i-1]) + function(x[i-2], y[i-2]))
        print(f"n = {i}: Corrector y_corrected = {y_corr:.6f}")

        # Store the corrected value
        y[i+1] = y_corr  # Ensure proper update

        # Compute exact solution and error
        y_exact[i+1] = exact_solution(x[i+1])
        error[i+1] = abs(y_exact[i+1] - y[i+1])

    # Print final result
    print(f"\nn = {n}: x = {x[n]:.4f}, y = {y[n]:.6f}")

    print("\nComparison with Euler's Method:")
    for i in range(n+1):
        print(f"n = {i}: x = {x[i]:.4f}, y_approx = {y[i]:.6f}, y_exact = {y_exact[i]:.6f}, Error = {error[i]:.6f}")

    return x, y

# Example usage
x0 = 0
y0 = 1
h = 0.1
x_end = 1

x_vals, y_vals = adams_bashforth_moulton(function, x0, y0, h, x_end)


