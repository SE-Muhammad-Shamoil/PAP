def enhanced_traffic_light(car_detected, pedestrian_waiting):
    
    if car_detected and pedestrian_waiting:
        print("Light is RED (Longer for pedestrians)")
    elif car_detected:
        print("Light is RED (Normal duration)")
    else:
        print("Light is GREEN")

# ----------------------------------------------- TEST CASES -------------

print("2. Enhanced Traffic Light")
enhanced_traffic_light(True, True)    # Car and pedestrian detected
enhanced_traffic_light(True, False)   # Only car detected
enhanced_traffic_light(False, False)  # No car or pedestrian