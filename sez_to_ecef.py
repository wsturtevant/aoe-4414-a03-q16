# sez_to_ecef.py
#
# Usage: python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km
#  Text explaining script usage
# Parameters:
#  o_lat_deg: 
#  o_lon_deg: 
#  o_hae_km: 
#  s_km:
#  e_km:
#  z_km:
#  
# Output:
#  
#
# Written by Wheat Sturtevant
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math
import numpy # matrix

# "constants"
# R_E_KM = 6378.137
# E_E = 0.081819221456

# initialize script arguments
o_lat_deg = float('nan')    # llh latitude in deg
o_lon_deg = float('nan')    # llh longitude in deg
o_hae_km = float('nan')     # height above the ellipse in km
s_km = float('nan')         # 
e_km = float('nan')         # 
z_km = float('nan')         # 

# parse script arguments
if len(sys.argv)==7:
    o_lat_deg = float(sys.argv[1])
    o_lon_deg = float(sys.argv[2])
    o_hae_km = float(sys.argv[3])
    s_km = float(sys.argv[4])
    e_km = float(sys.argv[5])
    z_km = float(sys.argv[6])
else:
    print(\
        'Usage: '\
        'python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km'\
    )
    exit()

# write script below this line
  
# initialize o_lat_rad, o_lon_rad 
o_lat_rad = o_lat_deg*(math.pi/180)
o_lon_rad = o_lon_deg*(math.pi/180)

# define R_y R_z and SEZ vector
R_y = numpy.array([[math.sin(o_lat_rad), 0, math.cos(o_lat_rad)],
                   [0.0, 1.0, 0.0],
                   [-math.cos(o_lat_rad), 0, math.sin(o_lat_rad)]])

R_z = numpy.array([[math.cos(o_lon_rad), -math.sin(o_lon_rad), 0],
                   [math.sin(o_lon_rad), math.cos(o_lon_rad), 0],
                   [0.0, 0.0, 1.0]])

SEZ = numpy.array([[s_km], [e_km], [z_km]])

# Rotations
rotation_1 = R_y.dot(SEZ)
rotation_2 = R_z.dot(rotation_1)
  
# calculate ecef_x_km ecef_y_km ecef_z_km
ecef_x_km = rotation_2[0]
ecef_y_km = rotation_2[1]
ecef_z_km = rotation_2[2]

# print outputs
print('ecef_x_km: '+str(ecef_x_km))
print('ecef_y_km: '+str(ecef_y_km))
print('ecef_z_km: '+str(ecef_z_km))

# Test Usage: 
# py sez_to_ecef.py 40.496 -80.246 0.0 0.0 1.0 0.3