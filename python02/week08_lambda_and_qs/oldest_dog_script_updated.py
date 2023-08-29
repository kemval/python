class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age


def main():

    dog1 = Dog("quesito", 5)
    dog2 = Dog("bartolome", 7)
    dog3 = Dog("piña", 4)

    find_oldest_age = lambda *dogs: max(dog.age for dog in dogs)
    oldest_dog_age = find_oldest_age(dog1, dog2, dog3)

    print(f"The oldest dog is aged {oldest_dog_age} years.")


main()
