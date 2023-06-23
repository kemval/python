import functions

students = []

while True:
    student_dict = {}
    functions.fill_grades(student_dict)
    students.append(student_dict)

    choice = input("Do you want to enter grades for another student? (yes/no): ")
    if choice.lower() != "yes":
        break

print("\nStudent Gradebook:\n")
for student in students:
    print("Name:", student["name"])
    print("Homeworks:", student["homework"])
    print("Quizzes:", student["quizzes"])
    print("Tests:", student["tests"])
    avg = functions.get_average(student)
    letter_grade = functions.get_letter_grade(avg)
    print("Letter Grade:", letter_grade)
    print()

class_avg = functions.get_class_average(students)
print("Class Average:", class_avg)