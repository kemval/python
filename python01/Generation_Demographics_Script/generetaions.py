name = input("What is your first name? ")
last_name = input("What is your last name? ")
age = int (input("How old are you? "))
current_year = int (2023)
print("Hello stranger! Let me give your data", name, last_name, "your current age is", age, "and you born back in", current_year - age)

if current_year - age <= 1965:
  print ("you are a baby boomer!")
elif current_year - age <= 1980:
  print ("you are a Generation x")
elif current_year - age <= 1996:
  print ("you are a Millenial")
elif current_year - age <= 2012:
  print ("you are Generation z")
else:
  current_year - age >= 2013
  print("too young!")
  