test_list = []
N = 4 
while True :    
    elements= input("enter elements or 'N' to exit: \n").title()
    test_list.append(elements)
    if elements.upper() == 'N':
        print("The last N elements of list are : " + str(res))  
        print("Bye")
        break
    res = test_list[-N:]


