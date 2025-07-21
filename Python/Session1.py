
num_students = int(input("How many students? "))

grades = {}
for i in range(num_students):
    name = input(f"Enter name for student {i+1}: ")
    grade = float(input(f"Enter grade for {name}: "))
    grades[name] = grade

print("\nAll students and their grades:")
for name, grade in grades.items():
    print(f"{name}: {grade}")


max_grade = max(grades.values())
for name, grade in grades.items():
    if grade == max_grade:
        print(f"\nHighest grade is {grade}, achieved by {name}")


average = sum(grades.values()) / num_students
print(f"\nAverage grade: {average:.2f}")


print("\nStudents who failed (grade < 50):")
for name, grade in grades.items():
    if grade < 50:
        print(f"{name}: {grade}")
