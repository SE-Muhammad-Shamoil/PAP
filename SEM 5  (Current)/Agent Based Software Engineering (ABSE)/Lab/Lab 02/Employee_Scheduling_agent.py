def calculate_shift_utility(shift, employee):
    weights = {'skill': 0.5, 'availability': 0.3, 'preference': 0.2}

    skill_score = 1 if shift['required_skill'] in employee['skills'] else 0

    availability_score = 1 if employee['availability'] == 'Available' else 0

    preference_score = 1 if shift['time'] in employee['preferences'] else 0

    utility = (weights['skill'] * skill_score +
               weights['availability'] * availability_score +
               weights['preference'] * preference_score)
    
    return utility

def assign_best_shift(shifts, employees):

    assignments = {}
    for shift in shifts:
        best_employee = None
        max_utility = -1

        for employee in employees:
            utility = calculate_shift_utility(shift, employee)
            print(f"  - Checking {employee['name']} for {shift['name']}: Utility = {utility:.2f}")
            if utility > max_utility:
                max_utility = utility
                best_employee = employee['name']
        
        assignments[shift['name']] = {'employee': best_employee, 'utility_score': max_utility}
        print(f"-> Best assignment for {shift['name']}: {best_employee} (Score: {max_utility:.2f})\n")
    return assignments

# --- Example Usage ---
print("\n--- Employee Scheduling Agent Demo ---")
shifts_to_fill = [
    {'name': 'Morning Shift', 'time': 'Morning', 'required_skill': 'Cashier'},
    {'name': 'Evening Shift', 'time': 'Evening', 'required_skill': 'Manager'}
]
employees_data = [
    {'name': 'Alice', 'skills': ['Cashier'], 'availability': 'Available', 'preferences': ['Morning']},
    {'name': 'Bob', 'skills': ['Manager'], 'availability': 'Available', 'preferences': ['Evening']},
    {'name': 'Charlie', 'skills': ['Cashier'], 'availability': 'Not Available', 'preferences': ['Morning']}
]

final_assignments = assign_best_shift(shifts_to_fill, employees_data)
print("--- Final Schedule ---")
for shift, details in final_assignments.items():
    print(f"{shift}: {details['employee']}")
    