# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon-deg hae_km
#  Converts LLH vector components to ECEF
# Parameters:
#  lat_deg: Latitude in degrees
#  lon_deg: Longitude in degrees
#  hae_km: Height above the equator in kilometers
# Output:
#  Prints ECEF components (x,y,z) in kilometers
#
# Written by Celia Sterthous
# Other contributors: None
#
# See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math 

# "constants"
R_E_KM = 6378.1363
E_E    = 0.081819221456

# helper functions

def calc_denom(ecc,lat_rad):
    return math.sqrt(1.0-(ecc**2)*(math.sin(lat_rad))**2)

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
lat_deg = float('nan')
lon_deg = float('nan')
hae_km  = 0.0

lat_rad = lat_deg*math.pi/180.0
lon_rad = lon_deg*math.pi/180.0
# parse script arguments
if len(sys.argv)==4:
  lat_deg = float(sys.argv[1])
  lon_deg = float(sys.argv[2])
  hae_km  = float(sys.argv[3])
else:
   print(\
      'Usage: '\
      'python3 llh_to_ecef.py lat_deg lon-deg hae_km'
     )
   exit()

# write script below this line
denom = calc_denom(E_E,lat_rad)
C_E = R_E_KM/denom
S_E = (R_E_KM*(1-E_E*E_E))/denom
r_x_km = (C_E+hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
r_y_km = (S_E+hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
r_z_km = (S_E+hae_km)*math.sin(lat_rad)
print('r_x_km: '+r_x_km)
print('r_y"km: '+r_y_km)
print('r_z_km: '+r_z_km)