"""This script aims to ensure the solver return a consistent trajectory"""

from App.module.orbit_propagator.solver import solve
import numpy as np
import matplotlib.pyplot as plt

print('Testing orbit propagator...\n')

boundary_dates = [0, 30000]
initial_data = [0, 8200, 0, 6, 6, 0]
display_times = np.linspace(0, 30000, 600)

sol = solve(boundary_dates, initial_data, display_times)

print('Exit code : {}'.format(sol.status))
print('Success : {}'.format(sol.success))
print('Exit message : {}'.format(sol.message))

xarray = sol.y[0]
yarray = sol.y[1]
zarray = sol.y[2]

plt.plot(xarray, yarray)
plt.show()
