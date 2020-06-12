"""This file contains function to solve numerically differential equation"""

# Importing required modules
from App.module.orbit_propagator.forces import *
from App.data.ephem import load, geocentric_position
from scipy.integrate import solve_ivp
import numpy as np


# Configure time frame
ts = load.timescale()
date = {
        'y': 2020,
        'm': 8,
        'd': 28,
        'h': 9,
        'min': 52,
        's': 0
    }


def f(t, y):
    """
f is the function of the ODE formulation dy/dt = f(t,y)
    :param y: state vector
    :param t: time variable
    :return: return derivation of the state vector according to Newton second law
    """
    time = ts.utc(date['y'], date['m'], date['d'], date['h'], date['min'], date['s'] + t)
    position = np.array([y[0], y[1], y[2]])
    moon_position = geocentric_position('moon', time)
    sun_position = geocentric_position('sun', time)
    resultant = earth_zonal_harmonics_gravity_force(position) + lunar_gravity_force(position, moon_position) \
        + solar_gravity_force(position, sun_position)
    return [y[3], y[4], y[5], resultant[0], resultant[1], resultant[2]]


def solve(boundary_dates, initial_data, display_times):
    """
This function solves the trajectory equation knowning the initial position and velocity and the time interval
where you compute the trajectory.
    :param boundary_dates: [t0, tf]
    :param initial_data: [x[t0], y[t0], z[t0], vx[t0], vy[t0], vz[t0]]
    :param display_times: a numpy array containing the times where you want to save the position
    :return: a fine mess
    """
    return solve_ivp(f, boundary_dates, initial_data, t_eval=display_times)
