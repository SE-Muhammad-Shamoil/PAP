def extended_seatbelt_alarm(seatbelt_fastened, car_moving):
    """
    Sounds an alarm only if the seatbelt is unfastened AND the car is moving.
    """
    if not seatbelt_fastened and car_moving:
        print("ALARM: Please Fasten Your Seatbelt!")
    elif not seatbelt_fastened and not car_moving:
        print("Reminder: Seatbelt is not fastened.")
    else:
        print("Seatbelt Fastened. Safe to drive.")

# ----------------------------------------------- TEST CASES -------------
print("6. Extended Seatbelt Alarm")
extended_seatbelt_alarm(False, True)   # Not fastened and moving
extended_seatbelt_alarm(False, False)  # Not fastened and stationary
extended_seatbelt_alarm(True, True)    # Fastened and moving