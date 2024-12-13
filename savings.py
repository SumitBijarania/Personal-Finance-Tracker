import sqlite3

def get_current_savings_amount():
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    
    # Sum all the current amounts for savings goals
    cursor.execute("SELECT SUM(current_amount) FROM savings_goals")
    current_savings = cursor.fetchone()[0] or 0  # Default to 0 if no savings exist
    
    conn.close()
    return current_savings

# Function to set and track savings goals
def set_savings_goal(goal_name, target_amount):
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO savings_goals (goal_name, target_amount, current_amount) VALUES (?, ?, ?)",
                   (goal_name, target_amount, 0))
    conn.commit()
    conn.close()


# Function to update savings goal progress
def update_savings_goal(goal_id, amount):
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    
    # Get the current savings goal details
    cursor.execute("SELECT target_amount, current_amount FROM savings_goals WHERE id = ?", (goal_id,))
    goal = cursor.fetchone()
    
    if goal:
        target_amount, current_amount = goal
        
        # Check if the target is already achieved
        if current_amount >= target_amount:
            print(f"Goal {goal_id} has already been completed.")
            conn.close()
            return
        
        # Calculate the remaining amount to reach the target
        remaining_amount = target_amount - current_amount
        
        # If the added amount exceeds the remaining amount, only add the required amount
        if amount > remaining_amount:
            print(f"Only {remaining_amount} is needed to complete the goal.")
            amount = remaining_amount  # Set the amount to the remaining required amount
        
        # Update the current amount with the new value
        cursor.execute("UPDATE savings_goals SET current_amount = current_amount + ? WHERE id = ?", (amount, goal_id))
        
        # Check if the goal is completed
        cursor.execute("SELECT current_amount FROM savings_goals WHERE id = ?", (goal_id,))
        updated_current_amount = cursor.fetchone()[0]
        
        # Mark the goal as completed if the target is reached
        if updated_current_amount >= target_amount:
            print(f"Goal {goal_id} is now completed!")
        
        conn.commit()
    conn.close()

# Function to list all savings goals
def list_savings_goals():
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, goal_name, target_amount, current_amount FROM savings_goals")
    goals = cursor.fetchall()
    
    if goals:
        print("\n--- Savings Goals ---")
        for goal in goals:
            status = "Completed" if goal[3] >= goal[2] else "In Progress"
            print(f"ID: {goal[0]}, Goal: {goal[1]}, Target: ${goal[2]}, Current Progress: ${goal[3]}, Status: {status}")
    else:
        print("\nNo savings goals found.")
    
    conn.close()
