# Expense Tracker

A simple command-line expense tracker written in Python.

## Features

- Add expenses with date, category, amount, and optional comment
- View all expenses in a neatly formatted table
- Display statistics including total expenses and breakdown by category
- Backup expenses data to JSON format
- Easy to use CLI interface

## Project Structure

```
expense_tracker/
├── data/
│ ├── expenses.csv # Stores expense records (auto-created)
│ └── backup.json # Backup file in JSON format
├── expense_tracker.py # Main CLI script
├── utils.py # Helper functions for file operations and display
├── README.md # This file
└── requirements.txt # Python dependencies
```

## Installation

1. Clone the repository:

git clone https://github.com/AkArtem/expense_tracker.git  
cd expense_tracker

2. Install dependencies:

pip install -r requirements.txt

## Usage

Run the main script:

python expense_tracker.py

Follow the menu options to add expenses, view all expenses, see statistics, backup data, or exit.

## Notes

- The `data/expenses.csv` file is created automatically when you add your first expense.  
- Backup files are saved as `data/backup.json`.  
- This project is intended as a simple CLI tool and does not have a graphical interface.

---