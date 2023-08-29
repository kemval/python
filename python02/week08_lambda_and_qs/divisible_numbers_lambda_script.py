numbers = [36, 32, 19, 65, 57, 39, 152, 639, 121, 44, 90, 190, 96, 102]

divisible = list(filter(lambda num: num % 8 == 0 or num % 13 == 0, numbers))

print("Numbers divisible by 8 or 13:", divisible)
