#python code for euler's method

def function(x, y):
    return 3*x*x*y

def euler(x0, x, y, h):
    
    while x0<x:
        
        y = y + h*function(x0, y)
        
        x0 = x0 + h
        
        print(f"The approximate solution of y at x == {'%.1f'%x0} is---> {'%.8f'%y}")
        
x0 = 0
x = 1
y = 1
h = 0.1

euler(x0, x, y, h)
    