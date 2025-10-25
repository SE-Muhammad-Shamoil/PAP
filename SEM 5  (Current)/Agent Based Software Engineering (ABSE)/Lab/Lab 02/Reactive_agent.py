def reactive_agent(environment_state):
    if environment_state == 'Obstacle on left':
        print(f"Perception: {environment_state}. Action: Move Right")
        return 'Move Right'
    elif environment_state == 'Obstacle on right':
        print(f"Perception: {environment_state}. Action: Move Left")
        return 'Move Left'
    else:
        print(f"Perception: {environment_state}. Action: Move Right (default)")
        return 'Move Right'

# --- Example Usage ---
print("--- Reactive Agent Demo ---")
reactive_agent('Obstacle on left')
reactive_agent('Obstacle on right')
reactive_agent('Clear')