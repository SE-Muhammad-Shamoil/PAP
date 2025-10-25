class ExtendedBattery:
    def __init__(self, charge=80):
        self.charge = charge

    def use(self, amount=25):
        if self.charge <= 10:
            print(f"CRITICAL BATTERY ({self.charge}%). Auto-powering off.")
        else:
            self.charge -= amount
            print(f"Using battery... Current charge: {self.charge}%")

    def recharge(self, amount=25):
        if self.charge >= 100:
            print(f"WARNING: Battery is full ({self.charge}%). Please unplug.")
        else:
            self.charge += amount
            if self.charge > 100: # Cap charge at 100
                self.charge = 100
            print(f"Recharging... Current charge: {self.charge}%")


# ----------------------------------------------- TEST CASES -------------
print("## 9. Extended Battery System ##")
battery = ExtendedBattery(90)
battery.recharge() # Recharges battery back to 100
battery.recharge() # Get Warning that battery is full
battery.use(95)    # Drains to 5
battery.use()      # Critical battery, powers off