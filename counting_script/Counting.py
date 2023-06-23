while True:
    number = int (input ("enter a number higher than 0: "))
    count = 1
    while count <= number:
        print(count)
        count += 1 
    check = input("would you like to enter another number? y or n: ")
    if check.lower () != "y":
        break
print("bye")

   


