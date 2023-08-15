class StudentError(Exception):
    pass

def student_information():

    scores = {}

    while True:

        try:

            first_name = input("Enter student's first name (or press Enter to finish): ")

            if not first_name:
                break
                
            last_name = input("Enter student's last name: ")
            score_str = input("Enter student's score: ")
            
            try:
                score = float(score_str)
                full_name = f"{first_name} {last_name}"
                scores[full_name] = scores.get(full_name, 0) + score

            except ValueError:

                raise StudentError("Enter a valid integer: " + score_str)
            
        except StudentError as e:
            print("Error:", e)
    
    return scores

def main():
    
    try:
        student_scores = student_information()
        
        sorted_scores = sorted(student_scores.items(), key=lambda x: x[1], reverse=True)
        
        print("Student Score Report:")
        for student, score in sorted_scores:
            print(f"{student}: {score:.2f}")
        
        file_name = input("Enter the name of the file: ")

        with open(file_name, 'w') as file:

            for student, score in sorted_scores:
                file.write(f"{student}: {score:.2f}\n")
        
        print(f"Report saved to {file_name}")

    except StudentError:
        pass


main()
