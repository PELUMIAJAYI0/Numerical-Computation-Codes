def segun(x, y):
    return 3 * x * x * y


def runge_kutta(x0, y, x, h):
    print("  x  | K1 | K2 | K3 | k4 | y ")
    print("_________________________________________________________________________")
    while x0 < x:
        k1 = segun(x0, y) # your value of k1
        xk = x0 + 0.5 * h
        yk2 = y + 0.5 * h * k1
        k2 = segun(xk, yk2) # your value of k2
        yk3 = y + 0.5 * k2
        k3 = segun(xk, yk3) 
        xk4 = x0 + h
        yk4 = y + h * k3
        k4 = segun(xk4, yk4)
        y = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x0 = x0 + h
        # print("The value of y at x is: ","%.1f"%x0, " is ", "%.8f"%y)
        print(
            "%.1f" % x0,
            " | ",
            "%.8f" % k1,
            " | ",
            "%.8f" % k2,
            " | ",
            "%.8f" % k3,
            " | ",
            "%.8f" % k4,
            " | ",
            "%.8f" % y,
        )


x0 = 0
y = 1
x = 1
h = 0.1

runge_kutta(x0, y, x, h)
