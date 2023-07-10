print ("Input lengths of the triangle sides ")
x_Value = float (input ("x: "))
y_Value = float (input ("y: "))
z_Value = float (input ("z: "))

if x_Value == y_Value == z_Value:
    print ("equilateral triangle")
elif x_Value == y_Value or y_Value == z_Value or z_Value == x_Value :
    print("isosceles triangle")    
else :
    print("scalene triangle")

