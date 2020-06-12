#! ../venv/scripts python3
# encoding: utf-8

"""This file launches the software with provided tools"""
from App.data.ephem import updateDataFiles
from App.module.orbit_propagator.solver import *
import matplotlib.pyplot as plt


# TODO Implement a logging system to detect automatically errors

def main():
    """ This function initialize and launch the app."""

    print('Welcome to LEOCET.\n')
    ts = updateDataFiles()

    time_simulation = int(input('Enter time simulation : '))
    boundary_dates = [0, time_simulation]

    print('Enter initial position vector (in km) in the geocentric frame : ')
    x = int(input('x : '))
    y = int(input('y : '))
    z = int(input('z : '))

    print('Enter initial velocity vector (in km/s) in the geocentric frame : ')
    vx = int(input('vx : '))
    vy = int(input('vy : '))
    vz = int(input('vz : '))
    initial_data = [x, y, z, vx, vy, vz]
    display_times = np.linspace(0, time_simulation, 1000)

    # Starting date of simulation
    date = {
        'y': 2020,
        'm': 8,
        'd': 28,
        'h': 9,
        'min': 52,
        's': 0
    }

    sol = solve(boundary_dates, initial_data, display_times, ts, date)

    print('Exit code : {}'.format(sol.status))
    print('Success : {}'.format(sol.success))
    print('Exit message : {}'.format(sol.message))

    xarray = sol.y[0]
    yarray = sol.y[1]
    zarray = sol.y[2]

    plt.plot(xarray, yarray)
    plt.show()


if __name__ == "__main__":
    main()
else:
    print("Error: this file is not a module or a package...")
