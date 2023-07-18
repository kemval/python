
username1 = input ("Please enter your username: ")
password1 = input("Please enter your password: ")

print ("Thank you for saving your data ", username1) 
print ("continue to sign in")

def main():

    username = input ("Please confirm your username: ")
    password = input("Please confirm your password: ")

    if username1 == username and password1 == password:  
        print("Logged in successfully as " + username)
        exit()

    else:    
        print ("incorrect data!")
    main()    
main()



