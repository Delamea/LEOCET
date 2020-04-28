"""This file contain all import constant use in the software"""

# Import functions required
from App.data.load import geocentric_position

# Constants definition
G = 6.67408 * 10 ** -20  # universal gravitational constant
M_T = 5.972 * 10 ** 24  # Earth mass
R_T = 6371 * 10 ** 3  # Earth Radius
M_L = 7.34767309 * 10 ** 22 # Lunar mass
M_S = 1.989 * 10 ** 30


class Body:
    """
Class defining a celestial object except a debris.
The attributes are the followings :
    name: string
    mass (in kg): integer
    average_radius (in km): integer
    equatorial_radius (in km): integer
    """

    # Initializer / Instance Attributes
    def __init__(self, name, mass, average_radius = None, equatorial_radius=None):
        self.name = name
        self.mass = mass
        self.average_radius = average_radius
        self.equatorial_radius = equatorial_radius

    # instance method
    def position(self, t):
        """
Compute the position of the body in the geocentric frame.
        :param t: seek time
        :return: vector position [x,y,z] where x, y, z are in km
        """
        return geocentric_position(self.name, t)
