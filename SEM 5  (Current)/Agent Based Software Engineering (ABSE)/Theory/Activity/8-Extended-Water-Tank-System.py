class ExtendedWaterTank:
    def __init__(self, level=50):
        self.level = level

    def fill(self, amount=15):
        if self.level >= 95:
            print(f"Water level is {self.level}%. Draining automatically to prevent overflow.")
            self.drain(20)
        else:
            self.level += amount
            print(f"Filling... Current level: {self.level}%")

    def drain(self, amount=15):
        if self.level < 20:
            print(f"WARNING: Low water at {self.level}%. Cannot drain further.")
        else:
            self.level -= amount
            print(f"Draining... Current level: {self.level}%")

# ----------------------------------------------- TEST CASES -------------
print("8. Extended Water Tank System")
tank = ExtendedWaterTank(85)
tank.fill() # Fills to 100
tank.fill() # Tries to fill more, but auto-drains first
tank.drain(70) # Drains to 10
tank.drain() # Tries to drain, but level is too low