import functiions

# Create 3 dictionaries that contain the following keys-values

"""student_list = {}
student_dic02 = {}
student_dic03 = {}"""
student_list= []

students_quantity = int (input("How many students are u adding? "))
count=0

while students_quantity <= count:
    count =+1
    for student in range ():
        
        name = functiions.generate_name(length=6)
        student_list.update({"name" : name})

    homework_quantity = int (input("How many homework grades are u adding? "))
    for homework in range (homework_quantity):
        homework = random.randint (0,100)
        homework += 1
        student_list.update({"Homework" : homework})

    quizzes_quantity = int (input("How many quizzes grades are u adding? "))    

    for quizzess in range (quizzes_quantity):
        quizzes = random.randint (0,100) 
        quizzes += 1
        student_list.update({"Quizzes" : quizzes})

    tests_quantity = int (input("How many test grades are u adding? "))    

    for tests in range (tests_quantity):
        test = random.randint (0,100) 
        test += 1
        student_list.update({"Tests" : test})

    print (student_list)
print("Please enter a number from 1 to 3")    

#     student_data[studentName]= subject_data

# def get_class_average(list):
#     scores = []    


