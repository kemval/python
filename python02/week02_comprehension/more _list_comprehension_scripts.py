# Use list comprehension to create a list with only the positive numbers from the list below and print the result.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive_list = [num for num in numbers if num >= 0]
print (positive_list)

# Create a nested list comprehension to find all numbers from 1 -1000 that are divisible by any digit between 2 and 9.

divisible_numbers = [num for num in range(1, 1001) if any(num % digit == 0 for digit in range(2, 10))]
print(divisible_numbers)



