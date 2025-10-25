def extended_sanitizer_dispenser(hand_detected, level):
 
    if level <= 10:
        print("ALERT: Sanitizer level is low! Please refill.")
    elif hand_detected:
        print("Dispensing Sanitizer")
    else:
        print("Waiting for Hand...")

# ----------------------------------------------- TEST CASES -------------
print("5. Extended Sanitizer Dispenser")
extended_sanitizer_dispenser(True, 5)    # Hand detected, but level is low
extended_sanitizer_dispenser(True, 50)   # Hand detected, level is OK
extended_sanitizer_dispenser(False, 50)  # No hand detected
