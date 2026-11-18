# Jalen Mitchell
# November 18, 2026
# P2HW1 - Travel Expenses
# This program asks the user for a travel budget, destination, and travel
# expenses. It calculates the total expenses and the money left in the budget.
#
# Pseudocode:
# 1. Ask the user to enter their travel budget.
# 2. Ask for the travel destination.
# 3. Ask for the amounts spent on gas, accommodation, and food.
# 4. Add the expenses to get the total expenses.
# 5. Subtract total expenses from the budget.
# 6. Display the destination and all money values in aligned columns,
#    with a dollar sign and two decimal places.

budget = float(input("Enter your budget: $"))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? $"))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? $"))
food = float(input("Last, how much do you need for food? $"))

total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

print()
print("--------------------Travel Expenses--------------------")
print(f"{'Location:':<25}{destination}")
print(f"{'Initial Budget:':<25}${budget:,.2f}")
print()
print("                  Fuel")
print(f"{'Gas:':<25}${gas:,.2f}")
print()
print("                 Accommodation")
print(f"{'Hotel:':<25}${accommodation:,.2f}")
print()
print("                    Food")
print(f"{'Food:':<25}${food:,.2f}")
print()
print("--------------------------------------------------------")
print(f"{'Total Expenses:':<25}${total_expenses:,.2f}")
print(f"{'Remaining Balance:':<25}${remaining_balance:,.2f}")
