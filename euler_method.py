def euler_method(f, x0, y0, h):
    x_values = [x0]
    y_values = [y0]
    while x0 < 1:
        y0 = y0 + h * f(x0, y0)
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

# Using Euler's Method to solve the differential equation
x_values, y_values = euler_method(f, x0, y0, h)

# Printing the result
print("Euler's Method: y(1) =", y_values[-1])
