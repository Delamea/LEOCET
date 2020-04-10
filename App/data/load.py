"""This file contains the function that download skyfield's data required by the software"""

# Import required methods
from skyfield.api import Loader, load

# Specify the targeted directory
load = Loader('./data', verbose=False)


def updateDataFiles():
    """Update Skyfield's data files."""
    print("Files are updating...")
    ts = load.timescale()
    planets = load('de421.bsp')
    print("Data files have been updated.")
