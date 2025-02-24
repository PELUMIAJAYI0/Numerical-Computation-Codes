"""
def function(x,y):
    return 3*x*x*y

def euler(x0, y, h, x):
    while x0 < x:
        y = y+h*function(x0, y)#euler method formula
        x0 = x0+h
        print("Approximate solution of y at x = ", '%.1f'%x0 ,"is, ","%.8f"%y )
    
x0 = 0
x = 1
h = 0.1
y = 1
euler(x0, y, h, x)


def function(x, y):
    return -x*(y+y*y)

def euler(x0, x, y,h):
    while x0< x:
        y = x+h * function(x0, y)
        x0 = x0+h
        print(f"The approximate solution of y at x =  {'%.1f'%x0} is {'%.8f'%y}")
        
x0 = 0
x = 1
y = 1
h = 0000.1
euler(x0, x, y, h)



def function(x, y):
    return -y

def euler(x0, x, y,h):
    while x0<x:
        y = x+h * function(x, y)
        x0 = x0 + h
        
        print(f"The approximate solution of y at x is---> {'%.1f'%x0} is {'%.8f'%y}") 
        
        
x0 = 0
x = 1
y = 1
h = 0.1

euler(x0, x, y, h)

"""