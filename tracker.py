import sqlite3
import datetime
from savings import get_current_savings_amount

# Function to add income
def add_income(description, amount):
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO income (description, amount, date) VALUES (?, ?, ?)", (description, amount, date))
    conn.commit()
    conn.close()

# Function to add expense
def add_expense(description, category, amount):
    # Get current savings progress before adding expense
    current_savings = get_current_savings_amount()
    
    # Check if the expense exceeds available savings progress
    if amount > current_savings:
        print("\nWarning: Expense exceeds your current savings progress! Expense not added.")
    else:
        # Proceed to add expense since it's within savings progress
        conn = sqlite3.connect('finance_tracker.db')
        cursor = conn.cursor()
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        cursor.execute("INSERT INTO expenses (description, category, amount, date) VALUES (?, ?, ?, ?)",
                       (description, category, amount, date))
        conn.commit()
        conn.close()
        
        # Deduct the expense from the savings goal
        conn = sqlite3.connect('finance_tracker.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE savings_goals SET current_amount = current_amount - ? WHERE current_amount >= ?", 
                       (amount, amount))
        conn.commit()
        conn.close()

# Function to view summary
def view_summary():
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(amount) FROM income")
    total_income = cursor.fetchone()[0] or 0
    
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total_expenses = cursor.fetchone()[0] or 0
    
    balance = total_income - total_expenses
    
    print(f"\nTotal Income: ${total_income}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Balance: ${balance}")
    
    conn.close()
