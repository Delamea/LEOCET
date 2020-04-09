"""This file contain function that compute the different forces"""

# Import provided files
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
