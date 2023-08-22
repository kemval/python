class Person:
    def __init__(self, name, id):

        self.name = name
        self.id = id
        
    def display_info(self):
        
        print(f"Name: {self.name}, ID: {self.id}")


class Student(Person):

    def __init__(self, name, id):
        super().__init__(name, id)
        self.grades = {}
        
    def add_grade(self, subject, score):
        self.grades[subject] = score


def grade_reporter(student):

    for subject in student.grades.keys():
        yield subject


def save_report(student):

    file_name = f"{student.name}.txt"

    with open(file_name, "w") as file:

        for subject in grade_reporter(student):
            file.write(subject + "\n")

    print(f"Grades were saved in {file_name}")


#Main
student1 = Student("Mr.Gio", "2001")
student2 = Student("Mr.Tortugita", "1003")

student1.add_grade("Python", 30)
student1.add_grade("Booleans", 80)
student1.add_grade("Lists", 79)

student2.add_grade("Vscode", 79)
student2.add_grade("Functions", 23)
student2.add_grade("Class", 99)

print("Student 1 grades:")
for subject in grade_reporter(student1):

    print(subject)

print("\nStudent 2 grades:")
for subject in grade_reporter(student2):

    print(subject)

save_report(student1)
save_report(student2)
