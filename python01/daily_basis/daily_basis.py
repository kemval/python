import socket
import datetime

while True:
    print("choose among following options\n")
    print("1- Ping a hostname or ping an IP address")
    print("2- current date in two formats")
    print("3- next 5 days from current date")
    print("4- your age based on DOB")
    print("5- Exit \n")
    option = input("Please choose an option number: ")
    if option == "1":
        while True:
            host = input("Please enter the hostname: ")
            if host.isnumeric():
                print("please enter a valid hostname")
            else:
                print (f"This is the IP address: {socket.gethostbyname(host)}\n\n")
                break
    elif option == "2":
            current_date = datetime.datetime.now()
            updatedFormat = current_date.strftime("%d/%m/%y ------- %d %B %Y")
            print (f"This is the current date in the updated format: {updatedFormat}\n\n")

    elif option == "3":
            base = datetime.datetime.now()
            print("here are the next five days\n")
            for x in range(1, 6):
              future = (base + datetime.timedelta(days=x))

              #####no entendi si era poner solo el nombre del dia o el nombre con la fecha entonces deje los dos en line 33 :p ##########

              newDate = future.strftime("%A------%m/%d/%Y") 
              print (f"{newDate}\n")
              
    elif option == "4":
            now = datetime.datetime.now()
            print("Enter your date of birth (DD-MM-YYYY)(do not forget hyphen):")
            dob_input = input()
            birthday = datetime.datetime.strptime(dob_input, "%d-%m-%Y")
            difference = now - birthday
            age_in_years = difference.days // 365
            print(f"You are {age_in_years} years old.\n\n")

    elif option == "5":
            print("Goodbye!")
            break
    else:
        print("Invalid option, please enter only numbers from 1 to 5")



          

            
                  