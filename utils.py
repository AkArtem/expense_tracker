import csv
from tabulate import tabulate
from collections import defaultdict

def read_expenses(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return list(csv.reader(file))
    except FileNotFoundError:
        return []

def write_expense(filename, data):
    try:
        with open(filename, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(data)
        print("Expense added!")
    except Exception as e:
        print(f"Error writing expense: {e}")
        raise
    
def show_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    headers = ["Date", "Category", "Amount", "Comment"]
    print(tabulate(expenses, headers=headers, tablefmt="grid"))
    print(f"\nTotal expenses shown: {len(expenses)}")

def show_statistics(expenses):
    if not expenses:
        print("No expenses to analyze")
        return

    total = 0
    by_category = defaultdict(float)

    for date, category, amount, comment in expenses:
        try:
            amount = float(amount)
        except ValueError:
            continue
        total += amount
        by_category[category] += amount

    print(f"\n=== EXPENSE STATISTICS ===")
    print(f"Total expenses: ${total:.2f}")
    print(f"Number of transactions: {len(expenses)}")

    print(f"\n=== EXPENSES BY CATEGORY ===")
    for category, amount in by_category.items():
        percentage = (amount / total) * 100
        print(f"  {category.capitalize()}: ${amount:.2f} ({percentage:.1f}%)")

    top_expenses = sorted(expenses, key=lambda x: float(x[2]), reverse=True)[:3]
    print(f"\n=== TOP 3 BIGGEST EXPENSES ===")
    for i, expense in enumerate(top_expenses, 1):
        print(f"  {i}. {expense[0]} | {expense[1].capitalize()} | ${expense[2]} | {expense[3]}")

    