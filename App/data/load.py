"""This file contains the function that download skyfield's data required by the software"""

# Import required methods
from skyfield.api import Loader, load, load_file

# Specify the targeted directory
load = Loader('./data', verbose=False)


def updateDataFiles():
    """Update Skyfield's data files."""
    print("Files are updating...")
    load.timescale()
    load('de421.bsp')
    print("Data files have been updated.")


def geocentric_position(body_name, time):
    """
Compute the position of a body in the geocentric frame.
    :param body_name: body whose position is looking for
    :param time: seek time
    :return: position vector [x,y,z] where x, y, z are in km
    """
    planets = load_file("C:/Users/Quentin DELAMEA/Documents/07 - Projet 1A/LEOCET/App/data/de421.bsp")
    body = planets[body_name]
    earth = planets['earth']

    body_position = body.at(time).position.km
    earth_position = earth.at(time).position.km
    return body_position - earth_position



