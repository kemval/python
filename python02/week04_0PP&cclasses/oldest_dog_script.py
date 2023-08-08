class Dog:

    def __init__(self, name, age):

        self.name = name
        self.age = age


def find_oldest_dog(dogo1, dogo2, dogo3):

    oldest_dog = dogo1

    if dogo2.age > oldest_dog.age:
        oldest_dog = dogo2
    if dogo3.age > oldest_dog.age:
        oldest_dog = dogo3

    return oldest_dog


def main():

    dog1 = Dog("quesito", 5)
    dog2 = Dog("bartolome", 7)
    dog3 = Dog("piña", 4)

    oldest_dog = find_oldest_dog(dog1, dog2, dog3)

    print(f"The oldest dog is {oldest_dog.name}, aged {oldest_dog.age} years.")


main()
