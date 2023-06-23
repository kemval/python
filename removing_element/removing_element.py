list = []
for i in range (7):
    elements= int (input("enter seven elements or 'N, to exit: \n"))
    if elements == 'N':
        print("bye")
    list.append(elements)
list = [x for (i,x) in enumerate (list) if i not in (1,4,5)]    
print ("this is you list without 1st, 2nd and 5th element:", list)
