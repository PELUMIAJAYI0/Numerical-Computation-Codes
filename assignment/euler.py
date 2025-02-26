def function(x, y):
    return 3*x*x*y

def euler(x0, x, y, h):
    while x0 < x:
        
        y = y + h*function(x0, y)

        print(f"The value of y at x = {x0:.1f} is {y:.8f}")
        print("")
        
        x0 = x0 + h
        
x0 = 0
y = 1
x = 1
h = 0.1

euler(x0, x, y, h)
        