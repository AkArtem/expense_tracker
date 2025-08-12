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
    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(data)
    print("Expense added!")
    
def show_expenses(expenses):
    if not expenses:
        print("You have no expenses")
        return
    headers = ["Date", "Category", "Amount", "Comment"]
    print(tabulate(expenses, headers=headers, tablefmt="grid"))

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

    print(f"\nTotal expenses: {total:.2f}")

    print("\nExpenses by category:")
    for categoryy, amountt  in by_category.items():
        print(f"  {categoryy}: {amountt:.2f}")

    top_expenses = sorted(expenses, key=lambda x: float(x[2]), reverse=True)[:3]
    print("\nTop 3 biggest expenses:")
    for el in top_expenses:
        print(f"  {el[0]} | {el[1]} | {el[2]} | {el[3]}")

    