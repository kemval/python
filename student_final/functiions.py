import random
import string
import sys

#Generates a random name

VOWELS = "aeiou"
CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))


def generate_name(lenght):
    word = ""
    for i in range(length):
        if i % 2 == 0:
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    return word

"""if __name__ == "__main__":
    try:
        count = int(sys.argv[1])
    except:
        count = 4

    try:
        length = int(sys.argv[2])
    except:
        length = 6

    for i in range(count):
        print(generate_name(length))"""
        


        


#Create a list that contains the names of the students.

student_names = [generate_name(length=6)]


# Function to calculate the average of a list

def average(lst):
    return sum(lst) / len(lst)


# Write a function average(list) that receives a list of numbers and returns the average of that list.

def get_average(dictionary):
    homework_avg = average(dictionary["homework"])
    quizzes_avg = average(dictionary["quizzes"])
    tests_avg = average(dictionary["tests"])
    
    # Weights
    homework_weight = 0.1
    quizzes_weight = 0.3
    tests_weight = 0.6
    
    weighted_average = (homework_avg * homework_weight) + (quizzes_avg * quizzes_weight) + (tests_avg * tests_weight)
    return weighted_average



def get_class_average(student_list):
    scores = []  # Empty list to store the scores

    for student in student_list:
        student_average = get_average(student)
        scores.append(student_average)

    class_average = average(scores)
    return class_average    



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
    



#Create a list that contains the names of the students.

student_names = [generate_name(length=6)]


# Function to calculate the average of a list

def average(lst):
    return sum(lst) / len(lst)


# Write a function average(list) that receives a list of numbers and returns the average of that list.

def get_average(dictionary):
    homework_avg = average(dictionary["homework"])
    quizzes_avg = average(dictionary["quizzes"])
    tests_avg = average(dictionary["tests"])
    
    # Weights
    homework_weight = 0.1
    quizzes_weight = 0.3
    tests_weight = 0.6
    
    weighted_average = (homework_avg * homework_weight) + (quizzes_avg * quizzes_weight) + (tests_avg * tests_weight)
    return weighted_average


