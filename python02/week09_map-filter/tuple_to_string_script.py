# Write a function (either normal or lambda) that converts a list of tuples to a list of strings.

def tuple_to_string(tuple_list):
    return list(map(lambda x: ' '.join(map(str, x)), tuple_list))

tuple_list = [(1, 2), (3, 4), (5, 6)]
string_list = tuple_to_string(tuple_list)
print(string_list)  


# Then write another function to convert the list of strings into a list of lists 

def list_of_lists(string_list):
    return list(map(lambda x: list(map(int, x.split())), string_list))

string_list = ['1 2', '3 4', '5 6']
list_of_lists = list_of_lists(string_list)
print(list_of_lists)