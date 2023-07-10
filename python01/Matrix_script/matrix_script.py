
Rows = int(input("Enter the number of rows:"))
Columns = int(input("Enter the number of columns:"))

matrix = []
print("Enter 9 numbers: ")
 
for i in range(Rows):        
    a =[]
    for j in range(Columns):     
         a.append(int(input()))
    matrix.append(a)
 
for i in range(Rows):
    for j in range(Columns):
        print(matrix[i][j], end = " ")
    print()
