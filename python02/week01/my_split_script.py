list_01 = []

def split(word):
    return word.split()

def list_append (list_01):
    if True:
        list_01.extend(split(word))
        print(list_01)
    return list_01    

word = input('Enter your sentence: ')

split_list = split(word)
list_append(list_01)