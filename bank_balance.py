# Author: Kael
# Date: 02/13/2026
# Title: Budget Analysis Program

budget = float(input("Enter your monthly budget: "))
total_expenses = 0

num_expenses = int(input("How many expenses do you want to enter? "))

for i in range(num_expenses):
    expense = float(input(f"Enter expense #{i+1}: "))
    total_expenses += expense

difference = budget - total_expenses

print("\n----- Budget Report -----")
if difference > 0:
    print(f"You are UNDER budget by ${difference:.2f}")
elif difference < 0:
    print(f"You are OVER budget by ${abs(difference):.2f}")
else:
    print("You are EXACTLY on budget!")
