import calculator

dictionary = {}

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:

    choice = input ("enter a choice: ")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == '1':
        sum = calculator.add(num1, num2)
        print(num1, "+", num2, "=", sum)
        dictionary.update({"sum":sum})

    elif choice == '2':
        subtract = calculator.subtract(num1, num2)
        print(num1, "-", num2, "=", subtract)
        dictionary.update({"subtract":subtract})

    elif choice == '3':
        multi = calculator.multiply(num1, num2)
        print(num1, "*", num2, "=", multi)
        dictionary.update({"Multiply":multi})

    elif choice == '4':
        divide = calculator.divide(num1, num2)
        print(num1, "/", num2, "=", divide)
        dictionary.update({"Divide":divide})
    else:
        print("Invalid Input")
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break
 


    