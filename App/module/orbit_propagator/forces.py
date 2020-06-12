"""This file contains function that compute the different forces"""

# Importing required modules
from App.module.orbit_propagator.constants import *
from numpy.linalg import norm
from math import sqrt, atan, sin, cos
import numpy as np
from scipy.special import legendre


def earth_spherical_gravity_force(position):
    """
Compute the gravity force of a perfect spherical earth
    :param position vector in the cartesian basis
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
    return (-1 * G * M_L) / (norm(position - lunar_position) ** 3) * (position - lunar_position)


def solar_gravity_force(position, solar_position):
    """
Compute the gravity force exerted by Sun on the body
    :param position: vector body position
    :param solar_position: vector Solar position
    :return: the force vector expressed in the geocentric frame
    """
    return (-1 * G * M_S) / (norm(solar_position - position) ** 3) * (position - solar_position)


def earth_zonal_harmonics_gravity_force(position):
    """
Compute the additional acceleration due to the non-sphericity of the earth adding the contribution of the first four zonal harmonics
    :param position: cartesian position in geocentric frame of the point where the force is computed
    :return: cartesian acceleration vector
    """
    r, theta, phi = cartesian_to_spherical_coordinates(position)

    P2 = legendre(2)
    P3 = legendre(3)
    P4 = legendre(4)
    D2 = P2.deriv()
    D3 = P2.deriv()
    D4 = P2.deriv()

    f_sphe = np.array([1 - (a_e/r) ** 2 * 3 * J2 * np.polyval(P2, sin(phi)) - (a_e/r) ** 3 * 4 * J3 * np.polyval(P3, sin(phi)) - (a_e/r) ** 3 * 5 * J4 * np.polyval(P4, sin(phi)),
                       0,
                       cos(phi)*((a_e/r) ** 2 * J2 * np.polyval(D2, sin(phi)) - (a_e/r) ** 3 * J3 * np.polyval(D3, sin(phi)) - (a_e/r) ** 3 * J4 * np.polyval(D4, sin(phi)))])

    return spherical_to_cartesian_coordinates(-1 * G * M_T / (r ** 2) * f_sphe, theta, phi)


def cartesian_to_spherical_coordinates(position):
    """
Given a position vector in a cartesian frame, returns the spherical coordinates corresponding
    :param position: cartesian position vector [x, y, z]
    :return: spherical position vector [r, theta, phi]
    """
    r = sqrt(position[0] ** 2 + position[1] ** 2 + position[2] ** 2)
    theta = None
    phi = None

    if position[2] == 0:
        theta = np.pi/2
    elif position[2] > 0:
        theta = np.arctan(sqrt(position[0] ** 2 + position[1] ** 2)/position[2])
    elif position[2] < 0:
        theta = np.pi + np.arctan(sqrt(position[0] ** 2 + position[1] ** 2) / position[2])

    if position[0] == 0 and position[1] > 0:
        phi = np.pi/2
    elif position[0] == 0 and position[1] < 0:
        phi = 3/2*np.pi
    elif position[0] > 0 and position[1] >= 0:
        phi = np.arctan(position[1]/position[0])
    elif position[0] < 0 and position[1] >= 0:
        phi = np.pi + np.arctan(position[1]/position[0])
    elif position[0] < 0 and position[1] < 0:
        phi = np.pi + np.arctan(position[1]/position[0])
    elif position[0] > 0 and position[1] < 0:
        phi = 2*np.pi + np.arctan(position[1]/position[0])

    return np.array([r, theta, phi])


def spherical_to_cartesian_coordinates(vector, theta, phi):
    """
Given a position vector in a spherical frame, returns the cartesian coordinates corresponding
    :param position: spherical position vector [r, theta, phi]
    :return: cartesian position vector [x, y, z]
    """
    transition_matrix = np.array([[sin(theta) * cos(phi), cos(theta) * sin(phi), -1 * sin(phi)],
                                  [sin(theta) * sin(phi), cos(theta) * sin(phi), cos(phi)],
                                  [cos(theta), -1 * sin(theta), 0]])
    return np.dot(transition_matrix, vector)


def drag(velocity, mass, surface, cx = 0.2):
    """
Compute the drag force exerted by the atmosphere on the body
    :param velocity: body velocity
    :param mass: body mass
    :param surface: axposed surface i.e surface of the debris projected on the plane perpendicular to the flow axis
    :param cx: drag coefficient (default value is 0.2 according the empirical mean)
    :return: the force vector expressed in the geocentric frame
    """
    # TODO complete the acceleration due to drag
    return


def SRP(position, mass, surface, k =1):
    """
Compute the solar radiation radiation force exerted by Sun radiations on the body
    :param position: body position
    :param mass: body mass
    :param surface: exposed surface i.e surface projected on the plane perpendicular to Earth-Sun axis
    :param k: coefficient characterizing the interaction between photons and the debris surface
    :return: the force vector expressed in the geocentric frame
    """
    # TODO complete the acceleration due to solar radiation pressure
    return
