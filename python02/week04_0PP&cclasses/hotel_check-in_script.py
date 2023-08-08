class Guest:

    def __init__(self, name, ID, age):

        self.name = name
        self.ID = ID
        self.age = age


def print_guest_list(guest_list):

    print("\nGuest List:")

    for index, guest in enumerate(guest_list):

        print(f"Index {index}: Name: {guest.name}, ID: {guest.ID}, Age: {guest.age}")

def get_valid_integer_input(prompt):

    while True:

        try:
            value = int(input(prompt))
            return value
        
        except ValueError:
            print("Please enter a valid integer.")

def main():

    guest_list = []

    while True:

        name = input("Enter guest's name (or 'E' to stop): ").title()

        if name.title() == "E":
            break

        ID = input("Enter guest's ID (cedula): ")

        while True:
            age = get_valid_integer_input("Enter guest's age: ")
            if age >= 0:
                break
            else:
                print("Please enter a valid positive integer.")


        guest = Guest(name, ID, age)
        guest_list.append(guest)

        print("\nGuest successfully registered!\n")
        print_guest_list(guest_list)

main()
