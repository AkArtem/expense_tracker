import json
from datetime import datetime
from utils import read_expenses, write_expense, show_expenses, show_statistics

DATA_FILE = "data/expenses.csv"
BACKUP_FILE = "data/backup.json"

ALLOWED_CATEGORIES = ["food", "transport", "entertainment", "utilities",
                      "health", "shopping", "education", "travel", "other"]

def main():
    print("Welcome to Expense Tracker!")
    print("Your personal finance management tool.")
    
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add expense")
        print("2. Show all expenses")
        print("3. Show recent expenses (last 5)")
        print("4. Show statistics")
        print("5. Backup to JSON")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()
        
        match choice:
            case "1":
                add_expense()
            case "2":
                expenses = read_expenses(DATA_FILE)
                show_expenses(expenses)
            case "3":
                show_recent_expenses()
            case "4":
                expenses = read_expenses(DATA_FILE)
                show_statistics(expenses)
            case "5":
                backup_to_json()
            case "6":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice! Please enter a number from 1 to 6")
        
def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    
    while True:
        category = input(f"Please input category ({', '.join(ALLOWED_CATEGORIES)}): ").strip().lower()
        if not category:
            print("Category cannot be empty. Please try again.")
            continue
        if category not in ALLOWED_CATEGORIES:
            print(f"Invalid category. Allowed categories: {', '.join(ALLOWED_CATEGORIES)}")
            continue
        break
    
    while True:
        try:
            amount_input = input("Please input amount: ").strip()
            amount = float(amount_input)
            if amount <= 0:
                print("Amount must be greater than 0. Please try again.")
                continue
            break
        except ValueError:
            print("Amount must be a valid number. Please try again.")
            continue

    comment = input("Input a comment for this expense: ").strip()
    if not comment:
        comment = "No comment"
    
    try:
        write_expense(DATA_FILE, [date, category, amount, comment])
        print(" Expense added successfully!")
    except Exception as e:
        print(f" Error adding expense: {e}")
    
def show_recent_expenses():
    """Show the last 5 expenses."""
    print("\n--- RECENT EXPENSES (Last 5) ---")
    expenses = read_expenses(DATA_FILE)
    
    if not expenses:
        print("No expenses found.")
        return
    
    recent_expenses = expenses[-5:] if len(expenses) > 5 else expenses
    show_expenses(recent_expenses)
    
def backup_to_json():
    try:
        expenses = read_expenses(DATA_FILE)
        if not expenses:
            print("No expenses to backup.")
            return
            
        with open(BACKUP_FILE, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4, ensure_ascii=False)
        print(f"   Backup saved to {BACKUP_FILE}")
        print(f"   Total expenses backed up: {len(expenses)}")
    except Exception as e:
        print(f" Backup failed: {e}")

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")
