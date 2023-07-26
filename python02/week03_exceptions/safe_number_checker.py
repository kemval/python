def safe_number_check(user_input, low_limit, high_limit):
    while True:
        try:
            value = int(input(user_input))
            if low_limit <= value <= high_limit:
                return value
            else:
                print("Error: the value is not within permitted range (min..max)")
        except ValueError:
            print("Error: wrong input, and ask the user to input the value again")


user_input = "Enter an integer between 1 and 100: "
low_limit = 1
high_limit = 100
result = safe_number_check(user_input, low_limit, high_limit)
print(f"Valid input: {result}")