rows = int(input("Enter number of rows: "))

for i in range(rows):
    for a in range(i+1):
        print("* ", end="")
    print("\n")
