# Define the cities and their direct connections based on the hint 
cities = {
    "Murree": ["Islamabad"],
    "Islamabad": ["Murree", "Rawalpindi"],
    "Rawalpindi": ["Islamabad", "Kallar Kahar"],
    "Kallar Kahar": ["Rawalpindi", "Chakwal"],
    "Chakwal": ["Kallar Kahar", "Sargodha"],
    "Sargodha": ["Chakwal", "Faisalabad"],
    "Faisalabad": ["Sargodha", "Lahore"],
    "Lahore": ["Faisalabad", "Multan"],
    "Multan": ["Lahore", "Sukkur"],
    "Sukkur": ["Multan", "Hyderabad"],
    "Hyderabad": ["Sukkur", "Karachi"],
    "Karachi": [] # Destination
}

# Start and goal cities [cite: 163]
current_city = "Murree"
goal_city = "Karachi"

print("Welcome to the City Path Finder Game!")
print(f"You are starting in {current_city}. Try to reach {goal_city}.\n")

# --- Game loop ---
# This loop logic is identical to the lab example [cite: 118-137]
while current_city != goal_city:
    print(f"You are currently in: {current_city}")
    
    # Check for dead end (should only be Karachi)
    if not cities[current_city]:
        print("You are at a dead end, but it's not the goal!")
        break
        
    print(f"Possible cities to move to: {', '.join(cities[current_city])}")
    
    # Get the user's move
    move = input("Where would you like to move? ").strip()
    
    # Check if the move is valid
    if move in cities[current_city]:
        current_city = move
        print(f"Moving to {current_city}...\n")
    else:
        print("Invalid move! You can only move to cities directly connected to your current city.\n")

# --- End of game ---
if current_city == goal_city:
    print(f"Congratulations! You reached {goal_city}!")