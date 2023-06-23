import datetime

x = datetime.datetime.now()
print ("This is the current date: \n" ,x.strftime("%B / %A %d / %Y"))

n = int (input("Enter how many days ahead: \n"))

future = x + datetime.timedelta(days=n)
print ("The future date is: \n" ,future.strftime("%B / %A %d / %Y"))

