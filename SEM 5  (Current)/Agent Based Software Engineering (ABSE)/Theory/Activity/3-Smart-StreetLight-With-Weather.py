def smart_street_light(time, motion, weather):
   
    if weather == "rainy":
        print("Weather is rainy. Street Light ON")
    elif time == "night":
        if motion:
            print("Night time with motion. Street Light is BRIGHT")
        else:
            print("Night time with no motion. Street Light is DIM")
    else:
        print("Day time, clear weather. Street Light OFF")

# ----------------------------------------------- TEST CASES -------------
print(" 3. Smart Street Light ")
smart_street_light("day", False, "rainy")  # Rainy day
smart_street_light("night", True, "clear")   # Motion at night
smart_street_light("night", False, "clear")  # No motion at night
smart_street_light("day", False, "clear")    # Clear day