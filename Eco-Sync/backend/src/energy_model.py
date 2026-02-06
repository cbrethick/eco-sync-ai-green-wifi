CO2_FACTOR = 0.475  # kg per kWh

def energy(power_percent):
    max_power = 10  # watts
    actual_power = max_power * (power_percent / 100)
    return actual_power  # Wh per hour

def co2(energy_wh):
    return (energy_wh / 1000) * CO2_FACTOR
