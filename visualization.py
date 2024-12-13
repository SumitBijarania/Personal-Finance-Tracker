import sqlite3
import matplotlib.pyplot as plt

# Function to visualize spending
def visualize_spending():
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    expenses = cursor.fetchall()
    
    categories = [expense[0] for expense in expenses]
    amounts = [expense[1] for expense in expenses]
    
    # Bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(categories, amounts, color='skyblue')
    plt.xlabel('Expense Categories')
    plt.ylabel('Amount Spent')
    plt.title('Spending by Category')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
    # Pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title('Spending Distribution')
    plt.axis('equal')
    plt.show()
    
    conn.close()
