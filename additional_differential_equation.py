def runge_kutta_method(f, x0, y0, h):
    x_values = [x0]
    y_values = [y0]
    while x0 < 100:
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h/2, y0 + k1/2)
        k3 = h * f(x0 + h/2, y0 + k2/2)
        k4 = h * f(x0 + h, y0 + k3)
        y0 = y0 + (k1 + 2*k2 + 2*k3 + k4) / 6
        x0 += h
        x_values.append(x0)
        y_values.append(y0)
    return x_values, y_values

# Define the differential equation: dy/dx = 10y - e^(-x)
def f2(x, y):
    return 10*y - 2.718281828459045**(-x)  # e^(-x) is approximately 2.718281828459045^(-x)

x0 = 0
y0 = 1/11
h = 0.01  # Use a smaller step size for more accurate results

# Using the Runge-Kutta Method to solve the additional differential equation
x_values, y_values = runge_kutta_method(f2, x0, y0, h)

# Printing the result
print("y(100) using Runge-Kutta Method:", y_values[-1])
