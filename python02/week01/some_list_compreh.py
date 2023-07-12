# Ejercicio 1

l1 = [1, 2, 3, 4, 5]
l2 = [num for num in range (1,6)]
print (l2)


# Ejercicio 2

lst = [num for num in range (1200,2001,130)]
print (lst)



# Ejercicio 3


def square():
    l1 = [2, 4, 6, 8, 10, 12, 14]
    squared = [i ** 2 for i in l1]
    return squared


l2 = [i for i in square() if i > 50]
print(l2)


# Ejercicio 4


dict = {"sedan":1500,"suv":2000,"pickup":2500,"minivan":1600,"van":2400,"semi":13600,"bycicle":7,"motorcycle":110}

selected_vehicules = [i.upper() for i , x in dict.items() if x < 5000]

print (selected_vehicules)

# Ejercicio 5

list1 = [i for i in range (0,21)]
print (list1)
list2 = [(i,'odd') if i % 2 != 0 else (i,'even') for i in list1]
print (list2)

