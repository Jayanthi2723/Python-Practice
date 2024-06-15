def runge_kutta_method(f, x0, y0, h):
    x_values = [x0]
    y_values = [y0]
    while x0 < 1:
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h/2, y0 + k1/2)
        k3 = h * f(x0 + h/2, y0 + k2/2)
        k4 = h * f(x0 + h, y0 + k3)
        y0 = y0 + (k1 + 2*k2 + 2*k3 + k4) / 6
        x0 += h
        x_values.append(x0)
        y_values.append(y0)
    return x_values, y_values

# Define the differential equation: dy/dx = x + y
def f(x, y):
    return x + y

# Initial conditions
x0 = 0
y0 = 1

# Step size (subintervals)
h = 0.1

# Using the Runge-Kutta Method to solve the differential equation
x_values, y_values = runge_kutta_method(f, x0, y0, h)

# Printing the result
print("Runge-Kutta Method: y(1) =", y_values[-1])
