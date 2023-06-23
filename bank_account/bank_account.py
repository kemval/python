balance = float(input("Please insert the balance to start: "))
users = [("Jose","jose123"),("Kiki","12kiki34")]
transactions = []

while True:
    user = str(input("Please enter your username: "))
    passw = str(input("Please enter your password: "))
    temp = (user,passw)
    salir = False
    for i in users:
        if i == temp:
            salir = True
            break
    if salir == True:
        break
    print("Invalid user")

print("Welcome to your bank account system")
while True:
    print("1- Deposit")
    print("2- withdraw")
    print("3- Exit")
    option = str(input("Please choose an option number: "))
    if option == "1":
        while True:
            temp = str(input("Please enter the amount to deposit: "))
            if temp.isnumeric():
                balance += float(temp)
                transactions.append(("Deposit",temp))
                print (f"Your new balance is: {balance}")
                break
            else:
                print("Invalid option, please enter only numbers")
    elif option == "2":
        while True:
            temp = str(input("Please enter the amount to withdraw: "))
            if temp.isnumeric():
                if (balance < float(temp)):
                    print (f"You don't have enough founds, your actual balance is {balance}")
                    continue
                balance -= float(temp)
                transactions.append(("Wthdraw",temp))
                print (f"Your new balance is: {balance}")
                break
            else:
                print("Invalid option, please enter only numbers")
    elif option == "3":
        print("Your transactions:",transactions)
        print("Goodbye!")
        break
    else:
        print("Invalid option, please enter only numbers from 1 to 3")



