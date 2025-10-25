class TaskSequencingAgent:
    def __init__(self, task_list):

        self.pending_tasks = task_list
        self.completed_tasks = []
        print(f"Agent initialized. Goal: Complete tasks in order -> {self.pending_tasks}")

    def perform_next_task(self):

        if not self.pending_tasks:
            print("Goal achieved! All tasks are complete.")
            return

        # Get the next task from the list
        next_task = self.pending_tasks.pop(0)
        
        # Perform the task
        print(f"Performing task: '{next_task}'...")
        
        # Update state
        self.completed_tasks.append(next_task)
        
        print(f"Completed Tasks: {self.completed_tasks}")
        print(f"Remaining Tasks: {self.pending_tasks}\n")


# --- Example Usage ---
print("\n--- Goal-Based Agent Demo ---")
tasks = ['Gather requirements', 'Design system', 'Implement features', 'Test and deploy']
agent = TaskSequencingAgent(tasks)

# Sequentially perform all tasks
while agent.pending_tasks:
    agent.perform_next_task()

# Check status after completion
agent.perform_next_task()