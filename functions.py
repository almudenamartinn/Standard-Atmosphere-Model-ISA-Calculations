import numpy as np

# Constants
R = 287.05  # Specific gas constant for dry air, J/(kg·K)
g = 9.80665  # Acceleration due to gravity, m/s^2
dT_dh = -6.5 / 1000  # Temperature lapse rate, K/m
ht = 11 * 10**3  # Tropopause altitude, m
T0 = 273.15  # Standard temperature at sea level, K
p0 = 0.101325  # Standard atmospheric pressure at sea level, Pa
rho0 = 1.225  # Standard air density at sea level, kg/m^3

# THEORY
"""
STANDARD CONDITIONS:
1. Standard Temperature: 0°C (273.15 K)
2. Standard Pressure: 101.325 kPa (1 atm)
3. Standard Density: 1.225 kg/m³

Lapse Rate:
- The lapse rate is the rate of temperature change with altitude.
- The ISA defines a lapse rate of -6.5°C per 1,000 meters (-6.5 K/km) for the troposphere.
"""

# Function to calculate temperature based on altitude
def ISA_T(h):
    """
    Calculate temperature at a given altitude using the ISA model.
    Args:
        h: Altitude in meters.
    Returns:
        Temperature in Kelvin (K).
    """
    return T0 + dT_dh * h if h <= ht else T0

# Function to calculate pressure based on altitude
def ISA_p(h):
    """
    Calculate pressure at a given altitude using the ISA model.
    Args:
        h: Altitude in meters.
    Returns:
        Pressure in Pascals (Pa).
    """
    if h <= ht:
        return p0 * (1 + (dT_dh * h / T0))**(-g / (R * dT_dh))
    else:
        return p0 * np.exp(-g * (h - ht) / (R * ISA_T(ht)))

# Function to calculate density based on altitude
def ISA_rho(h):
    """
    Calculate air density at a given altitude using the ISA model.
    Args:
        h: Altitude in meters.
    Returns:
        Density in kilograms per cubic meter (kg/m^3).
    """
    if h <= ht:
        return rho0 * (1 + (dT_dh * h / T0))**(-g / (R * dT_dh))
    else:
        return rho0 * np.exp(-g * (h - ht) / (R * ISA_T(ht)))

################################
# INVERSE FUNCTIONS
# Calculate altitude based on atmospheric parameters

# Inverse function for temperature
def inv_ISA_T(T):
    """
    Calculate altitude from a given temperature using the ISA model.
    Args:
        T: Temperature in Kelvin (K).
    Returns:
        Altitude in meters (m).
    """
    return (T - T0) / dT_dh

# Inverse function for pressure
def inv_ISA_p(p):
    """
    Calculate altitude from a given pressure using the ISA model.
    Args:
        p: Pressure in Pascals (Pa).
    Returns:
        Altitude in meters (m).
    """
    return ht + (np.log(p0) - np.log(p)) * R * T0 / (g * dT_dh) if p <= p0 else 0

# Inverse function for density
def inv_ISA_rho(rho):
    """
    Calculate altitude from a given density using the ISA model.
    Args:
        rho: Density in kilograms per cubic meter (kg/m^3).
    Returns:
        Altitude in meters (m).
    """
    return ht + np.log(rho0 / rho) * R * T0 / (g * dT_dh) if rho <= rho0 else 0