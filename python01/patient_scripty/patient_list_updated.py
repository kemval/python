import getpass



print ("🫧 🪻 ♡︎ ~。.:* 🫧 ~ ♡︎ 🪻。.:* 🫧 ~ ♡︎ ~ 。.: 🪻 *🫧° ~ ⟡ ♡︎ ~  。 🪻 .:*🫧♡︎ ♡︎ 🫧 。.:* ~ ♡︎  ~     🪻     ♡︎ ~  🫧 ♡︎~ 。.:* 🪻 ~° ~ ♡︎ ⟡。.:* 🫧 🪻。.: 🫧 *~° ⟡ ♡︎ ~ 。 🪻 .:*🫧° ⟡ ♡︎ ♡︎ 🪻    🫧   ·  🪻 ♡︎~ 。.:* 🫧 ~° ⟡ ♡︎~ 🪻🫧 🪻 ♡︎ ~。.:* 🫧 ~ ♡︎ 🪻。.:* 🫧 ~ ♡︎ ~ 。.: 🪻 *🫧° ~ ⟡ ♡︎ ~  。 🪻 .:*🫧♡︎ ♡︎ 🫧 。.:* ~ ♡︎  ~     🪻     ♡︎ ~  🫧 ♡︎~ 。.:* 🪻 ~° ~ ♡︎ ⟡。.:* 🫧 🪻。.: 🫧 *~° ⟡ ♡︎ ~ 。 🪻 .:*🫧° ⟡ ♡︎ ♡︎ 🪻    🫧   ·  🪻 ♡︎~ 。.:* 🫧 ~° ⟡ ♡︎~ 🪻🫧 🪻 ♡︎ ~。.:* 🫧 ~ ♡︎ 🪻。.:* 🫧 ~ ♡︎ ~ 。.: 🪻 *🫧° ~ ⟡ ♡︎ ~  。 🪻 .:*🫧♡︎ ♡︎ 🫧 。.:* ~ ♡︎  ~     🪻     ♡︎ ~  🫧 ♡︎~ 。.:* 🪻 ~° ~ ♡︎ ⟡。.:* 🫧 🪻。.:H E L L O ! 🫧 *~° ⟡ ♡︎ ~ 。 🪻 .:*🫧° ⟡ ♡︎ ♡︎ 🪻    🫧   ·  🪻 ♡︎~ 。.:* 🫧 ~° ⟡ ♡︎~ 🪻🫧 🪻 ♡︎ ~。.:* 🫧 ~ ♡︎ 🪻。.:* 🫧 ~ ♡︎ ~ 。.: 🪻 *🫧° ~ ⟡  W E L C O M E ♡︎ ~  。 🪻 .:*🫧♡︎ ♡︎ 🫧 。.:* ~ ♡︎  ~     🪻     ♡︎ ~  🫧 ♡︎~ 。.:* 🪻 ~° ~ ♡︎ ⟡。.:* 🫧 🪻。.: 🫧 *~° U S E R !⟡ ♡︎ ~ 。 🪻 .:*🫧° ⟡ ♡︎ ♡︎ 🪻    🫧   ·  🪻 ♡︎~ 。.:* 🫧 ~° ⟡ ♡︎~ 🪻🫧 🪻 ♡︎ ~。.:* 🫧 ~ ♡︎ 🪻。.:* 🫧 ~ ♡︎ ~ 。.: 🪻 *🫧° ~ ⟡ ♡︎ ~  。 🪻 .:*🫧♡︎ ♡︎ 🫧 。.:* ~ ♡︎  ~     🪻     ♡︎ ~  🫧 ♡︎~ 。.:* 🪻 ~° ~ ♡︎ ⟡。.:* 🫧 🪻。.: 🫧 *~° ⟡ ♡︎ ~ 。 🪻 .:*🫧° ⟡ ♡︎ ♡︎ 🪻    🫧   ·  🪻 ♡︎~ 。.:* 🫧 ~° ⟡ ♡︎~ 🪻"
)

# Here is where the data will store

username_password = {}      
patient_list = []

# Now lets get the values from the user

username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")

# #Here where the magic happens, this will help us add the previous values to the database in dictionary order

username_password[username] = password

#lets verified the user to show patient list

while True:
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    if username in username_password and password == username_password[username]: 
        print("\nLogged in, welcome!\n")
        while True:
            print ("\nMenu")
            print ("\n1 Add name\n2 delete Name\n3 view your patient list\n4 log out\n")
            option = input("choose option: ")
            while True:
                if option == "1":
                    patient_names= input("\nadd name: \n").title()
                    # if patient_names == str:
                    patient_list.append(patient_names)
                    patient_list.sort()
                    patient_list = list(dict.fromkeys(patient_list))
                    break
                elif option == "2":
                    print ("\nThis is your current list")
                    print (f"{patient_list} \n")
                    question = input ("\nenter the name you woud like to remove: \n").title()
                    patient_list.remove (question)
                    print (f"\nhere is the updated list: {patient_list}\n")
                    break
                elif option == "3":
                    print ("\nThis is what you got so far: \n")
                    print (patient_list)
                    break    
                elif option == "4":
                    print("\nyou are log out, bye!\n")
                    print ("🫧 🪻 ♡︎ ~。.:* 🫧 ~ ♡︎ 🪻。.:* 🫧 ~ ♡︎ ~ 。.: 🪻 *🫧° ~ ⟡ ♡︎ ~  。 🪻 .:*🫧♡︎ ♡︎ 🫧 。.:* ~ ♡︎  ~     🪻     ♡︎ ~  🫧 ♡︎~ 。.:* 🪻 ~° ~ ♡︎ ⟡。.:* 🫧 🪻。.: 🫧 *~° ⟡ ♡︎ ~ 。 🪻 .:*🫧° ⟡ ♡︎ ♡︎ 🪻    🫧   ·  🪻 ♡︎~ 。.:* 🫧 ~° ⟡ ♡︎~ 🪻🫧 🪻 ♡︎ ~。.:* 🫧 ~ ♡︎ 🪻。.:* 🫧 ~ ♡︎ ~ 。.: 🪻 *🫧° ~ ⟡ ♡︎ ~  。 🪻 .:*🫧♡︎ ♡︎ 🫧 。.:* ~ ♡︎  ~     🪻     ♡︎ ~  🫧 ♡︎~ 。.:* 🪻 ~° ~ ♡︎ ⟡。.:* 🫧 🪻。.: 🫧 *~° ⟡ ♡︎ ~ 。 🪻 .:*🫧° ⟡ ♡︎ ♡︎ 🪻    🫧   ·  🪻 ♡︎~ 。.:* 🫧 ~° ⟡ ♡︎~ 🪻🫧 🪻 ♡︎ ~。.:* 🫧 ~ ♡︎ 🪻。.:* 🫧 ~ ♡︎ ~ 。.: 🪻 *🫧° ~ ⟡ ♡︎ ~  。 🪻 .:*🫧♡︎ ♡︎ 🫧 。.:* ~ ♡︎  ~     🪻     ♡︎ ~  🫧 ♡︎~ 。.:* 🪻 ~° ~ ♡︎ ⟡。.:* 🫧 🪻。.🫧 *~° ⟡ ♡︎ ~ 。 🪻 .:*🫧° ⟡ ♡︎ ♡︎ 🪻    🫧   ·  🪻 ♡︎~ 。.:* 🫧 ~° ⟡ ♡︎~ 🪻🫧 🪻 ♡︎ ~。.:* 🫧 ~ ♡︎ 🪻。.:* 🫧 ~ ♡︎ ~ 。.: 🪻 *🫧° ~ ⟡♡︎ ~  。 🪻 .:*🫧♡︎ ♡︎ 🫧 。.:* ~ ♡︎  ~     🪻     ♡︎ ~  🫧 ♡︎~ 。.:* 🪻 ~° ~ ♡︎ ⟡。.:* 🫧 🪻。.: 🫧 *~°⟡ ♡︎ ~ 。 🪻 .:*🫧° ⟡ ♡︎ ♡︎ 🪻    🫧   ·  🪻 ♡︎~ 。.:* 🫧 ~° ⟡ ♡︎~ 🪻🫧 🪻 ♡︎ ~。.:* 🫧 ~ ♡︎ 🪻。.:* 🫧 ~ ♡︎ ~ 。.: 🪻 *🫧° ~ ⟡ ♡︎ ~  。 🪻 .:*🫧♡︎ ♡︎ 🫧 。.:* ~ ♡︎  ~     🪻     ♡︎ ~  🫧 ♡︎~ 。.:* 🪻 ~° ~ ♡︎ ⟡。.:* 🫧 🪻。.: 🫧 *~° ⟡ ♡︎ ~ 。 🪻 .:*🫧° ⟡ ♡︎ ♡︎ 🪻    🫧   ·  🪻 ♡︎~ 。.:* 🫧 ~° ⟡ ♡︎~ 🪻")
                    exit() 
    else:   
        print("incorrect username / password, please try again")


            
