yesChoices = ["yes", "y"]
noChoices = ["no","n"]

info = input ("would you like to convert from centimiter to inches? ")
if info.lower () in yesChoices :
    cm = float (input ("enter the centimeters you would like to convert: "))
    inchDistance = cm / 2.54
    print("your distance in inches is: " , inchDistance )
elif info.lower () in noChoices :
    inch = float (input ("enter the inches you would like to convert into centimiters: "))
    cmDistance = inch / 0.39
    print("your distance in centimiters is: " , cmDistance )

else:
    print("no correct answer")