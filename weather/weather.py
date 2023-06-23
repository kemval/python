import random,datetime
while True:
    tuuple = ("Sunny", "Cloudy", "Windy", "Foggy", "Rainy")
    name = input ("What's ur name :3 ? for exit enter N \n")
    date = datetime.datetime.now().strftime("%A")
    weather = random.choice(tuuple)
    if name == "n" or name == "N":
       print ("bye")
       break
    elif name.isnumeric():
        print("Enter a valid name")
        break
    else:  
      print ("*********************************************")
      print (f"Hello {name}!")
      print (f"Today is {date}")
      print (f"The weather for today is {weather}")
      print ("*********************************************")
      continue
