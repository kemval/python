line_filled_numbers = input('Enter a line filled with numbers (must be separated by a white space): ').split()
list = [float(num) for num in line_filled_numbers]
total_sum = sum(list)
print(list)
print('Sum of float numbers:', total_sum)
