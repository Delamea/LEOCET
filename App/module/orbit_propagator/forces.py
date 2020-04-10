"""This file contains function that compute the different forces"""

# Importing required modules
from App.module.orbit_propagator.constants import *


# Forces expressions

def earth_spherical_gravity_force(x):
    """
Compute the gravity force of a perfect spherical earth
    :param x: position vector in the cartesian basis
    :return: the force vector expressed in the cartesian basis
    """
    f = (-1 * G * M_T) / ((x[0] ** 2 + x[1] ** 2 + x[2] ** 2) ** (3 / 2))  # Term appearing on all axes
    return [f * x[0], f * x[1], f * x[2]]


def solar_gravity(position, solar_position):
    return (-1 * G * M_S) / (norm(solar_position - position) ** 3) * (solar_position - position)


