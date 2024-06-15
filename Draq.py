import matplotlib.pyplot as plt
import numpy as np

def plot_circle(center, radius):
  x_points = np.linspace(center[0] - radius, center[0] + radius, 100)
  y_points = np.linspace(center[1] - radius, center[1] + radius, 100)
  plt.plot(x_points, y_points)

center = (1, -1)
radius = np.sqrt(2)
plot_circle(center, radius)

plt.show()
