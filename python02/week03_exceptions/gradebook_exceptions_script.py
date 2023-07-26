def add_grade(gradebook):
    while True:
        grade_input = input("Enter a grade (1-100) or 'q' to exit: ")
        if grade_input.lower() == 'q':
            return True

        try:
            grade = int(grade_input)
            if 1 <= grade <= 100:
                gradebook.append(grade)
            else:
                print("Grade should be between 1 and 100.")
        except ValueError:
            print("Please enter a valid number or 'q' to exit.")


def calculate_highest(gradebook):
    if not gradebook:
        raise ValueError("Gradebook is empty")
    return max(gradebook)


def calculate_lowest(gradebook):
    if not gradebook:
        raise ValueError("Gradebook is empty")
    return min(gradebook)


def calculate_average(gradebook):
    if not gradebook:
        raise ValueError("Gradebook is empty")
    return sum(gradebook) / len(gradebook)


def main():
    gradebook = []
    while True:
        q_requested = add_grade(gradebook)
        if q_requested:
            break

    if gradebook:
        print(f"\nGrades: {gradebook}")
        try:
            print(f"Highest Grade: {calculate_highest(gradebook)}")
            print(f"Lowest Grade: {calculate_lowest(gradebook)}")
            print(f"Average Grade: {calculate_average(gradebook)}")
        except ValueError as e:
            print(e)



main()
