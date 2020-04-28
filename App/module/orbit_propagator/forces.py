"""This file contains function that compute the different forces"""

# Importing required modules
from App.module.orbit_propagator.constants import *
from numpy.linalg import norm


def earth_spherical_gravity_force(position):
    """
Compute the gravity force of a perfect spherical earth
    :param x: position vector in the cartesian basis
    :return: the force vector expressed in the geocentric frame
    """
    return (-1 * G * M_T) / (norm(position) ** 3) * position


def lunar_gravity_force(position, lunar_position):
    """
Compute the gravity force exerted by Moon on the body
    :param position: vector body position
    :param lunar_position: vector lunar position
    :return: the force vector expressed in the geocentric frame
    """
    return (-1 * G * M_L)/(norm(position - lunar_position) ** 3) * (position - lunar_position)


def solar_gravity_force(position, solar_position):
    """
Compute the gravity force exerted by Sun on the body
    :param position: vector body position
    :param solar_position: vector Solar position
    :return: the force vector expressed in the geocentric frame
    """
    return (-1 * G * M_S) / (norm(solar_position - position) ** 3) * (position - solar_position)
