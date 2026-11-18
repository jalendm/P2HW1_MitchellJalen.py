# Jalen Mitchell
# November 18, 2026
# P2HW2 - Lists and Grades
# This program collects six module grades, stores them in a list, and
# displays the lowest grade, highest grade, sum, and average.

# Pseudocode:
# 1. Ask the user to enter a grade for Modules 1 through 6.
# 2. Store each grade in a separate variable.
# 3. Put all six grades into a list named grades.
# 4. Use min() to find the lowest grade.
# 5. Use max() to find the highest grade.
# 6. Use sum() to calculate the total of the grades.
# 7. Divide the total by the number of grades to calculate the average.
# 8. Display the results with the average rounded to two decimal places.

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

grades = [module1, module2, module3, module4, module5, module6]

lowest_grade = min(grades)
highest_grade = max(grades)
total_grades = sum(grades)
average_grade = total_grades / len(grades)

print()
print("---------------- Results ----------------")
print(f"{'Lowest Grade:':<20}{lowest_grade:g}")
print(f"{'Highest Grade:':<20}{highest_grade:g}")
print(f"{'Sum of Grades:':<20}{total_grades:g}")
print(f"{'Average:':<20}{average_grade:.2f}")
