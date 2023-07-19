

#ZeroDivisionError: float division by zero in Python
#The Python "ZeroDivisionError: float division by zero" occurs when we try to divide a floating-point number by 0.


#_________________________________________________

a = 15.0
b = 0

result = a / b

#_________________________________________________

a = 15.0
b = 0

try:
    result = a / b
except ZeroDivisionError:
    result = 0

print(result) 


