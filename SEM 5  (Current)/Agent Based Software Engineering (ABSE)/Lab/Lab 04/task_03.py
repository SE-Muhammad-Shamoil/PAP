def simulate_and_gate(): #AND SIMULATION
    print("\n--- AND Gate: Office Door Access ---")
    print("You must have BOTH a keycard AND the correct PIN.")
    
    has_keycard = input("Do you have the keycard? (yes/no): ").strip().lower()
    knows_pin = input("Do you know the PIN? (yes/no): ").strip().lower()
    
    # AND condition: Both must be true 
    if has_keycard == "yes" and knows_pin == "yes":
        print(">>> Access Granted. Welcome!")
    else:
        print(">>> Access Denied. Both a keycard and PIN are required.")

def simulate_or_gate(): #OR SIMULATION
    print("\n--- OR Gate: Street Lights Control ---")
    print("Lights turn on if it's dark OR if the manual override is on.")
    
    is_dark = input("Is it dark outside? (yes/no): ").strip().lower()
    is_manual_override = input("Is the manual override switch on? (yes/no): ").strip().lower()
    
    # OR condition: Either one (or both) can be true
    if is_dark == "yes" or is_manual_override == "yes":
        print(">>> Street lights are ON.")
    else:
        print(">>> Street lights are OFF.")

#-----RUN-----------
simulate_and_gate()
simulate_or_gate()