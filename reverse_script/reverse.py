list = []
while (True):
    elements= input("build your sentence or 'n' to stop: \n").title()
    if elements == 'N':
        list.reverse()
        print ("here is your build sentence in reverse ", list)
        print ("bye")
        continue
    list.append(elements)
    
    
    
  