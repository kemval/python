eCodes = ["404","500","418","No Error"]
emessage = ["Not Found","Internal Server Error","I'm a teapot","SUCCESS"]
print ('********************************')

print("*********Error script**********")
print ('********************************')

while True:
    print("\n\nOption 1")
    print("Option 2")
    print("Option 3")
    print("Option 4")
    print("Exit   5\n\n")
    option = input("Please choose an option: ")

    if option == "1":
            while True:
              if option > "5":
                print("Invalid option, please enter only numbers from 1 to 5")
              else:  
                print ('********************************')
                print (f"Error while executing task {option}")
                print (f"Error Number: {eCodes[0]}")
                print (f"Message: {emessage[0]}")
                print ('********************************')
                break

    elif option == "2":
            while True:
              if option > "5":
                  print("Invalid option, please enter only numbers from 1 to 5")
              else:
                  print ('********************************')
                  print (f"Error while executing task {option}")
                  print (f"Error Number: {eCodes[1]}")
                  print (f"Message: {emessage[1]}")
                  print ('********************************')
                  break
              
    elif option == "3":
            while True:
              if option > "5":
                  print("Invalid option, please enter only numbers from 1 to 5")
              else:    
                  print ('********************************')
                  print (f"Error while executing task {option}")
                  print (f"Error Number: {eCodes[2]}")
                  print (f"Message: {emessage[2]}")  
                  print ('********************************')
                  break
              
    elif option == "4":
            while True:
              if option > "5":
                  print("Invalid option, please enter only numbers from 1 to 5")
              else:    
                  print ('********************************')
                  print (f"Error while executing task {option}")
                  print (f"Error Number: {eCodes[3]}")
                  print (f"Message: {emessage[3]}")
                  print ('********************************')
                  break
                
    elif option == "5":
            print ('********************************')
            print("Goodbye!")
            print ('********************************')
            break
    else:
            print("Invalid option, please enter only numbers from 1 to 5")



