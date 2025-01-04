altitude = 5000  # Altitude in meters
temperature = ISA_T(altitude)
pressure = ISA_p(altitude)
density = ISA_rho(altitude)

print(f"At {altitude} m: T = {temperature} K, p = {pressure} Pa, rho = {density} kg/m^3")
