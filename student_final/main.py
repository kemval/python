import functiions

students = []
repeat = True
while True:
  
    while repeat:
        student_dict = {}
        functiions.fill_grades(student_dict)
        students.append(student_dict)

        choice = input("Do you want to enter grades for another student? (yes/no): ")
        if choice.lower() != "yes":
            repeat = False

    print("\nStudent Gradebook:\n")
    for student in students:
        print("Name:", student["name"])
        print("Homeworks:", student["homework"])
        print("Quizzes:", student["quizzes"])
        print("Tests:", student["tests"])
        avg = functiions.get_average(student)
        letter_grade = functiions.get_letter_grade(avg)
        print("Letter Grade:", letter_grade)
        print()

    class_avg = functiions.get_class_average(students)
    print("Class Average:", class_avg)

    choice = input("Do you want to create another gradebook? (yes/no): ")
    if choice.lower() != "yes":
        break
