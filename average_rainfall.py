# Author: Kael
# Date: 02/13/2026
# Title: Average Rainfall Program

total_rainfall = 0
months = 0

years = int(input("Enter the number of years: "))

for year in range(1, years + 1):
    print(f"\nYear {year}:")
    for month in range(1, 12 + 1):
        rainfall = float(input(f"  Enter rainfall for month {month}: "))
        total_rainfall += rainfall
        months += 1

average = total_rainfall / months

print("\n----- Rainfall Report -----")
print(f"Total months: {months}")
print(f"Total rainfall: {total_rainfall} inches")
print(f"Average rainfall per month: {average:.2f} inches")
