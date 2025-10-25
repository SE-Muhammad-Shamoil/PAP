def upgraded_automatic_door(motion_detected, person_standing_near):
   
    if motion_detected:
        print("Door Opens")
    elif not motion_detected and person_standing_near:
        print("Door Remains Open")
    else:
        print("Door Closes")

# ----------------------------------------------- TEST CASES -------------
print("## 1. Upgraded Automatic Door ##")
upgraded_automatic_door(True, True)    # Motion detected
upgraded_automatic_door(False, True)   # No motion, but person is near
upgraded_automatic_door(False, False)  # No motion, no one near