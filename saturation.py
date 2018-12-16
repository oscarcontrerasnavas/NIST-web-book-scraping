# Import GetAntoineCoef because it return the antoine coefficients for using
# them into the calcs
from antoine import get_antoine_coef

# Import the log10 function from Math module
from math import log10

def get_saturation_pressure(Name, Temperature):

    """ Return the value of the vapor pressure in bar at Temperature

    :param Name:
        String with the name of the substance in english.

    :param Temperature:
        float number of the temperature in Kelvin.

    :rtype float
    
    :return vapor_pressure
    
    """

    # Obtaining the antoine coefficients [A,B,C]
    [A, B, C] = get_antoine_coef(Name, Temperature)

    # Calculating the vapor_pressure from log10(Psat) = A - B/(Temperature + C)
    vapor_pressure = 10 ** (A - B/(Temperature + C))
    
    return vapor_pressure