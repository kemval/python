import random

def fill_grades(dictionary):
    dictionary["name"] = input("Enter student's name: ")
    dictionary["homework"] = [random.randint(0, 100) for _ in range(4)]
    dictionary["quizzes"] = [random.randint(0, 100) for _ in range(3)]
    dictionary["tests"] = [random.randint(0, 100) for _ in range(2)]


def average(lst):
    return sum(lst) / len(lst) if len(lst) > 0 else 0


def get_average(dictionary):
    homework_avg = average(dictionary["homework"])
    quizzes_avg = average(dictionary["quizzes"])
    tests_avg = average(dictionary["tests"])

    weighted_avg = 0.1 * homework_avg + 0.3 * quizzes_avg + 0.6 * tests_avg
    return weighted_avg


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def get_class_average(students):
    scores = []
    for student in students:
        avg = get_average(student)
        scores.append(avg)
    return average(scores)

