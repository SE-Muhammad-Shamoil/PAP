class ExtendedSmartThermostat:
    def __init__(self):
        self.previous_temp = None
        self.ideal_range = (19, 25)

    def update_state(self, current_temp):
        if self.previous_temp is None:
            print(f"Setting initial temperature to {current_temp}°C...")
        elif self.ideal_range[0] <= current_temp <= self.ideal_range[1]:
            print(f"Temperature {current_temp}°C is ideal. Turning systems OFF.")
        elif current_temp > self.previous_temp and current_temp > self.ideal_range[1]:
            print(f"It's getting hotter ({current_temp}°C)! Turning on the AC.")
        elif current_temp < self.previous_temp and current_temp < self.ideal_range[0]:
            print(f"It's cooling down ({current_temp}°C)! Turning on the heater.")
        else:
            print(f"Temperature is steady at {current_temp}°C.")
        self.previous_temp = current_temp

# ----------------------------------------------- TEST CASES -------------
print("7. Extended Smart Thermostat")
thermostat = ExtendedSmartThermostat()
thermostat.update_state(28) # Initial setup -> Hot
thermostat.update_state(22) # Cooling down into ideal range
thermostat.update_state(15) # Cooling down -> Heater ON