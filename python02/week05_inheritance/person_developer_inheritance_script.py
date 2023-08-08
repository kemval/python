class Person:

    def __init__(self, firstname, lastname, phone_number, hobbies):

        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number
        self.hobbies = hobbies

    def full_name(self):

        return f"{self.firstname} {self.lastname}"

    def additional_info(self):

        return {"phone_number": self.phone_number, "hobbies": self.hobbies}


class Developer(Person):

    def __init__(self, firstname, lastname, phone_number, hobbies, github_username, expertise):

        super().__init__(firstname, lastname, phone_number, hobbies)

        self.github_username = github_username

        self.expertise = expertise

    def welcome(self):

        print(f"Welcome, {self.full_name()}! Your area of expertise is {self.expertise}.")

        print(f"GitHub Username: {self.github_username}")


developer_instance = Developer("Gio", "SuperMaster", "888-888-SENSEI",
                               ["Better than you", "Hablame cuando seas un rockstar"],
                               "Python4life", "Being the Best developer ever")


print("\nFull Name:", developer_instance.full_name())
additional_info = f"\n{developer_instance.additional_info()}\n"
print(f"\nAdditional Info:, {additional_info}\n")
developer_instance.welcome()
print("\n")
