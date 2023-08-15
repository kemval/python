def count(content):

    characters_count = {}

    for char in content:

        if char.isalpha():

            char = char.lower()

            characters_count[char] = characters_count.get(char, 0) + 1

    return characters_count

def histogram(characters_count):

    sorted_chars = sorted(characters_count.keys())

    for char in sorted_chars:

        print(f"{char}: {'$' * characters_count[char]}")

def save_histogram(file_name, characters_count):

    histogram_name = file_name + "_hist.txt"
    
    with open(histogram_name, 'w') as hist_file:

        sorted_chars = sorted(characters_count.keys())

        for char in sorted_chars:
            hist_file.write(f"{char}: {'$' * characters_count[char]}\n")

def main():

    file_name = input("Enter the name of the file: ")

    try:

        with open(file_name, 'r') as file:

            content = file.read()
            characters_count = count(content)
            
            if characters_count:

                print("Character Histogram:")
                histogram(characters_count)
                
                save_histogram(file_name, characters_count)
                print(f"Histogram saved to {file_name}_hist.txt")

            else:

                print("No alphabetical characters found in the file.")

    except FileNotFoundError:

        print("File not found.")


main()