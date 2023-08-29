add_grade = lambda gradebook: [gradebook.append(int(grade)) for grade in iter(lambda: input("Enter a grade (1-100) or 'q' to exit: "), 'q') if grade.isdigit() and 1 <= int(grade) <= 100]



calculate_highest = lambda gradebook: max(gradebook) if gradebook else None

calculate_lowest = lambda gradebook: min(gradebook) if gradebook else None

calculate_average = lambda gradebook: sum(gradebook) / len(gradebook) if gradebook else None

def main():
    
    gradebook = []
    add_grade(gradebook)
    
    if gradebook:
        print(f"\nGrades: {gradebook}")
        try:
            print(f"Highest Grade: {calculate_highest(gradebook)}")
            print(f"Lowest Grade: {calculate_lowest(gradebook)}")
            print(f"Average Grade: {calculate_average(gradebook)}")
        except ValueError as e:
            print(e)
            

main()
