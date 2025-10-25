import random

# Winning State
goal_state = [[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 0]]

def generate_puzzle(): #Generation of random puzzle
    nums = list(range(9)) # Numbers 0 to 8
    random.shuffle(nums)
    return [nums[0:3], nums[3:6], nums[6:9]]

def find_zero(state): #locating zero state or empty space
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return

def print_puzzle(state): #Print puzzle
    print() 
    for row in state:
        print("  ".join(str(num) if num != 0 else " " for num in row))
    print() 

def move(state, direction): #Control of empty state
    i, j = find_zero(state)
    new_state = [row[:] for row in state] 

    if direction == "up" and i > 0:
        # Swap with tile above
        new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
    
    elif direction == "down" and i < 2: # Boundary changed from 1 to 2
        # Swap with tile below
        new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
    
    elif direction == "left" and j > 0:
        # Swap with tile to the left
        new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
    
    elif direction == "right" and j < 2: # Boundary changed from 1 to 2
        # Swap with tile to the right
        new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
    
    else:
        print("Invalid move! Try again.")
    
    return new_state

print("--- 3x3 Sliding Puzzle ---")
puzzle = generate_puzzle()

while puzzle != goal_state:
    print_puzzle(puzzle)
    move_direction = input("Move (up/down/left/right): ").strip().lower()
    
    if move_direction in ["up", "down", "left", "right"]:
        puzzle = move(puzzle, move_direction)
    else:
        print("Invalid input. Please enter 'up', 'down', 'left', or 'right'.")

print("\n--- Solved! ---")
print_puzzle(puzzle)
print("Congratulations! You solved it!")