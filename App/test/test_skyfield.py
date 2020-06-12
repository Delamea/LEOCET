"""This script aims to ensure that data collected with Skyfield are coherent"""

import sys
from numpy.linalg import norm
from App.data.ephem import *

print("Testing skyfield.py...\n")

ts = updateDataFiles()

earthSunDist = norm(geocentric_position('sun',     ts.now()))
print('Distance Earth-Sun : {}'.format(earthSunDist))

if 147100000 < earthSunDist < 152100000:
    print('Correct value.\n')
else:
    print('Wrong value...')
    sys.exit(1)


earthMoonDist = norm(geocentric_position('moon',     ts.now()))
print('Distance Earth-Moon : {}'.format(earthMoonDist))

if 356410 < earthMoonDist < 405500:
    print('Correct value.\n')
else:
    print('Wrong value...')
    sys.exit(1)

print('Skyfield testing statue : OK')
