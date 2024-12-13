import sqlite3

def create_db():
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    
    # Create tables for income, expenses, and savings goals
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS income (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            amount REAL,
            date TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            category TEXT,
            amount REAL,
            date TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS savings_goals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            goal_name TEXT,
            target_amount REAL,
            current_amount REAL
        )
    ''')
    
    conn.commit()
    conn.close()
