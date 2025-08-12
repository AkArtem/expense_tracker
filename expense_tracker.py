import json
from datetime import datetime
from utils import read_expenses, write_expense, show_expenses, show_statistics

DATA_FILE = "data/expenses.csv"
BACKUP_FILE = "data/backup.json"

def main():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add expense")
        print("2. Show all expenses")
        print("3. Show statistics")
        print("4. Backup to JSON")
        print("5. Exit")

        choise = input("Choose an option (1-5): ").strip()
        
        match choise:
            case "1":
                add_expense()
            case "2":
                expenses = read_expenses(DATA_FILE)
                show_expenses(expenses)
            case "3":
                expenses = read_expenses(DATA_FILE)
                show_statistics(expenses)
            case "4":
                backup_to_json()
            case "5":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice! Please enter a number from 1 to 5")
        
def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Please input category: ").strip()
    
    try:
        amount = float(input("Please input amount: ").strip())
        if amount <= 0:
            print("Amount must be greater than 0")
            return
    except ValueError:
        print("Amount must be a number")
        return

    comment = input("Input a comment for this expense: ").strip()
    
    write_expense(DATA_FILE, [date, category, amount, comment])
    
def backup_to_json():
    with open(BACKUP_FILE, "w", encoding="utf-8") as file:
        expenses = read_expenses(DATA_FILE)
        json.dump(expenses, file, indent=4, ensure_ascii=False)
        print(f"Backup saved to {BACKUP_FILE}")

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")