# Jade Tran
# 10/12/24
# P2HW2
# Creating lists

# Pseudocode:
# 1. Ask the user to input grades for six modules.
# 2. Store the grades in a list.
# 3. Find the lowest grade in the list.
# 4. Find the highest grade in the list.
# 5. Calculate the sum of the grades.
# 6. Calculate the average of the grades.
# 7. Display the lowest grade, highest grade, sum, and average (formatted to two decimal places).

grades = []

for i in range(1, 7):
    grade = float(input(f"Enter grade for Module {i}: "))
    grades.append(grade)

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

print("\n------------Results------------")
print(f"Lowest Grade:        {lowest_grade:.2f}")
print(f"Highest Grade:       {highest_grade:.2f}")
print(f"Sum of Grades:       {sum_of_grades:.2f}")
print(f"Average:       {average_grade:.2f}")
print("---------------------------------")
