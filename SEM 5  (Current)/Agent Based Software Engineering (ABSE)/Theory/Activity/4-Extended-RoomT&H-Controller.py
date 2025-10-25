def extended_temp_control(temp, humidity):
    
    # Temperature control
    if temp < 18:
        print("Heater ON")
    elif temp > 26:
        print("AC ON")
    else:
        print("Temperature is OK")
    
    # Humidity control
    if humidity > 60:
        print("High humidity detected. Dehumidifier ON")
    else:
        print("Humidity is OK")

# ----------------------------------------------- TEST CASES -------------
print("4. Extended Temperature Controller ")
extended_temp_control(15, 70) # Too cold and humid
extended_temp_control(30, 50) # Too hot, humidity ok
extended_temp_control(21, 65) # Temp ok, too humid