a_list = []
maxList = 5
n = 3
while (maxList>0):
    numbers= int (input("Enter 5 numbers grater than 0:\n"))
    a_list.append(numbers)
    a_list.sort()
    maxList -= 1
result = a_list[-n:]
print("The highest three numbers are: ", result)
print("The sum of the highest three numbers is: ", sum(result)) 

import math
product = math.prod (result)
print("The product of the highest three numbers is: ", product)