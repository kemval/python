list = []
for i in range(0, 10):
    num = int(input('Enter Number 10 numbers grater than 0:\n'))
    list.append (num)
    if num % 2 != 0:
      my_final_list = set(list)
      print(my_final_list, "these are odd numbers")
    else:
      print(num, "is not odd")    
