"""
Expense Tracker
Uso de funciones lambda para cálculo de gastos
"""

expenses = [
    ("Food", 120),
    ("Transport", 50),
    ("Entertainment", 80)
]

total_expenses = sum(map(lambda expense: expense[1], expenses))

print("Total expenses:", total_expenses)
