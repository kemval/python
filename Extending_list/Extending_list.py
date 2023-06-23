letters = input("Enter letters with a space: \n")
letters = letters.upper()
letter_list = letters.split(" ")

n = int(input("Enter a value for n: ")) 

for letter in letter_list:
    for i in range(1, n+1):
        print(f"{letter}{i}", end=" ")