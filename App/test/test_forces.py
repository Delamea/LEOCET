"""This script aims to ensure that functions calculating forces return consistent values. This is done by using
theoretical formulas or tabulated data. """


import sys
from App.module.orbit_propagator.forces import *
from App.data.ephem import *
from App.module.orbit_propagator.constants import *

print('Testing forces computed values...\n')

ts = updateDataFiles()

g = norm(earth_spherical_gravity_force(np.array([R_T, 0, 0])))
print('Acceleration of gravity on the ground : {}'.format(g))

if norm(g - 9.8196*10**-3)/(9.8196*10**-3) < 0.01:
    print('Consistent value.\n')
else:
    print('Inadmissible value.')
    sys.exit(1)


lunarAccelerationAtEarth = norm(lunar_gravity_force(np.array([0, 0, 0]), geocentric_position('moon',     ts.now())))
print('Lunar acceleration at Earth center : {}'.format(lunarAccelerationAtEarth))

if 2.9823 * 10 ** -8 < lunarAccelerationAtEarth < 3.8605 * 10 ** -8:
    print('Consistent value.\n')
else:
    print('Inadmissible value.')
    sys.exit(1)


solarAccelerationAtEarth = norm(solar_gravity_force([0, 0, 0], geocentric_position('sun', ts.now())))
print('Solar acceleration at Earth center : {}'.format(solarAccelerationAtEarth))

if 5.7380 * 10 ** -6 < solarAccelerationAtEarth < 6.1348 * 10 ** -6:
    print('Consistent value.\n')
else:
    print('Inadmissible value.')
    sys.exit(1)


northCartPosition = np.array([0, 0, R_T])
northSphPosition = cartesian_to_spherical_coordinates(northCartPosition)
print('North position in spherical frame : {}'.format(northSphPosition))

southCartPosition = np.array([0, 0, -R_T])
southSphPosition = cartesian_to_spherical_coordinates(southCartPosition)
print('South position in spherical frame : {}'.format(southSphPosition))

eastCartPosition = np.array([0, R_T, 0])
eastSphPosition = cartesian_to_spherical_coordinates(eastCartPosition)
print('East position in spherical frame : {}'.format(eastSphPosition))

westCartPosition = np.array([0, -R_T, 0])
westSphPosition = cartesian_to_spherical_coordinates(westCartPosition)
print('West position in spherical frame : {}'.format(westSphPosition))

frontCartPosition = np.array([R_T, 0, 0])
frontSphPosition = cartesian_to_spherical_coordinates(frontCartPosition)
print('Front position in spherical frame : {}'.format(frontSphPosition))

backCartPosition = np.array([-R_T, 0, 0])
backSphPosition = cartesian_to_spherical_coordinates(backCartPosition)
print('Back position in spherical frame : {}'.format(backSphPosition))

pointCartPosition = np.array([R_T, -R_T, -R_T])
pointSphPosition = cartesian_to_spherical_coordinates(pointCartPosition)
print('Point position in spherical frame : {}'.format(pointSphPosition))

gCorrected = earth_zonal_harmonics_gravity_force(np.array([0, R_T, 0]))
print('Acceleration of gravity on the ground with harmonics corrections : {}'.format(gCorrected))
