check_starts_with = lambda string, char: string.title().startswith(char.title())

user_input = input("Enter a string: ")

while True:
    start_char = input("Enter the character to check if the string starts with: ")
    if not start_char.isnumeric() and len(start_char) == 1:
        break
    else:
        print("Please enter a single non-numeric character.")

try:
    result = check_starts_with(user_input, start_char)
    print("Output:", result)
except AttributeError:
    print("Please enter a valid character.")
