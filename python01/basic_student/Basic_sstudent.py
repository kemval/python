gradebook = []
for i in range (5):
    name = input (f"Enter the name of student {i+1}: ")
    grades = []

    for j in range(3):
        grade = int (input (f"Enter Grade {j+1}:"))
        grades.append(grade)
    gradebook.append((name, grades))

for student in gradebook:
    name, grades = student
    avg_grade = sum(grades) / 3
    print (f"{name} received grades of {grades[0]}, {grades[1]}, and {grades[2]}, with an average grade of {avg_grade:.2f}.")