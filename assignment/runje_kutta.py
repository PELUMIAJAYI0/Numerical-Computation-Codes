def function(x, y):
    return 3*x*x*y

def runje_kutta(x0, x, y, h):
    while x0 < x:
        
        k1 = function(x0, y)
        
        k2 = function(x0 + 0.5*h, y + 0.5*h*k1)
        
        k3 = function(x0 + 0.5*h, y + 0.5*h*k2)
        
        k4 = function(x0 + h, y + h*k3)
        
        y = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        
        print(f"The value of y at x = {x0:.1f} is {y:.8f}")
        print("")
        
        x0 = x0 + h
        
x0 = 0
y = 1
x = 1
h = 0.1

runje_kutta(x0, x, y, h)