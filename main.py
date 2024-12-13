from database import create_db
from tracker import add_income, add_expense, view_summary
from savings import set_savings_goal, update_savings_goal, list_savings_goals
from visualization import visualize_spending

def menu():
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Set Savings Goal")
        print("5. Update Savings Goal")
        print("6. Visualize Spending")
        print("7. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            description = input("Enter income description: ")
            amount = float(input("Enter income amount: "))
            add_income(description, amount)
        
        elif choice == '2':
            description = input("Enter expense description: ")
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            add_expense(description, category, amount)
        
        elif choice == '3':
            view_summary()
        
        elif choice == '4':
            goal_name = input("Enter savings goal name: ")
            target_amount = float(input("Enter target amount: "))
            set_savings_goal(goal_name, target_amount)
        
        elif choice == '5':
            # List existing savings goals before updating
            list_savings_goals()
            goal_id = int(input("Enter the ID of the goal to update: "))
            amount = float(input("Enter amount to add to this goal: "))
            update_savings_goal(goal_id, amount)
        
        elif choice == '6':
            visualize_spending()
        
        elif choice == '7':
            print("Exiting the program...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    create_db()
    menu()
