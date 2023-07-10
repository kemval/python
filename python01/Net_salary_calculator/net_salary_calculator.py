name = input("What is your name: ")
salary = float (input("Enter your salary: "))
ccss = float ((salary * 10.6) / 100)
bp = float ((salary * 1.5) / 100)
neto = float ((salary - ccss) - bp)
print("Hello stranger!", name,"let me give you your numbers")
print("after the CCSS deduction you have: ", ccss)
print("after the Banco Popular deduction you have: ", bp)
print("your net salary is the following: ", neto)


