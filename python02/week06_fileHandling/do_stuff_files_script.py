def create_file(file_name):

    with open(file_name, 'w') as file:

        for line in range(10):
            file.write(f"This is line {line + 1}\n")

def read_file_into_list(file_name):

    with open(file_name, 'r') as file:

        lines = file.readlines()

    return [line.strip() for line in lines]            

def read_first_n_lines(file_name, n):

    with open(file_name, 'r') as file:
        lines = [next(file).strip() for _ in range(n)]
        
    return lines

def read_last_n_lines(file_name, n):

    with open(file_name, 'r') as file:

        lines = file.readlines()[-n:]

    return [line.strip() for line in lines]

def append_text_to_file(file_name, text):

    with open(file_name, 'a') as file:

        file.write(text)

def main():

    file_name = "sample.txt"
    create_file(file_name)

    while True:
        print("\nMenu:")
        print("1. Read first n lines")
        print("2. Add text and display")
        print("3. Read last n lines")
        print("4. Read entire file into list")
        print("5. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":

            n = int(input("Enter the number of lines to read: "))
            lines = read_first_n_lines(file_name, n)
            print("\n".join(lines))

        elif choice == "2":
            text_to_add = input("Enter text to add: ")
            append_text_to_file(file_name, text_to_add + "\n")
            print(f"Text added: '{text_to_add}'")

        elif choice == "3":
            n = int(input("Enter the number of lines to read: "))
            lines = read_last_n_lines(file_name, n)
            print("\n".join(lines))

        elif choice == "4":
            lines = read_file_into_list(file_name)
            print("\n".join(lines))

        elif choice == "5":
            break

        else:
            print("Please select a valid option.")


main()
