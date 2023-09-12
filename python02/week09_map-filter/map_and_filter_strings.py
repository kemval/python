# Filter Vowels in a String:

def filter_vowels(string):
    vowels = "AEIOUaeiou"
    return ''.join(filter(lambda x: x not in vowels, string))

input_string = "Hello Gio"
filtered_string = filter_vowels(input_string)
print(filtered_string) 

# Map and Filter to Add 2000 to Numbers Below 8000

def add_2000_numbers_below_8000(numbers):
    return list(map(lambda x: x + 2000, filter(lambda x: x < 8000, numbers)))

number_list = [1000, 5000, 9000, 6000, 3000]
result_list = add_2000_numbers_below_8000(number_list)
print(result_list) 

# Split a Dictionary of Lists into a List of Dictionaries

def split_dict_of_lists(dict_of_lists):
    return list(map(lambda x: {key: [value] for key, value in x.items()}, dict_of_lists))

dict_of_lists = {'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}
list_of_dicts = split_dict_of_lists(dict_of_lists)
print(list_of_dicts) 

# Convert Case of Characters in a Sequence

def convert_case(sequence, target_case='lower'):
    if target_case == 'lower':
        return list(map(lambda x: x.lower(), sequence))
    elif target_case == 'upper':
        return list(map(lambda x: x.upper(), sequence))
    else:
        return sequence

input = ['Hello', 'Gio']
lowercase= convert_case(input, 'lower')
print(lowercase) 
uppercase = convert_case(input, 'upper')
print(uppercase) 

# Convert Negative Numbers to Positive and Create a List with Converted Numbers

def convert_negatives_to_positive(numbers):
    return list(map(lambda x: abs(x), filter(lambda x: x < 0, numbers)))

number_list = [-5, 10, -15, 20, -25]
positive_list = convert_negatives_to_positive(number_list)
print(positive_list)  
