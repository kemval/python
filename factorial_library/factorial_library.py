import random
import math
while True:
  x = int (input("What's x? \n"))
  print (f"The factorial of {x} is", math.factorial(x))
  print (f"Your random number between 0 and {x} is", random.randint(0,x))




