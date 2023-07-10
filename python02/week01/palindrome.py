
def palindrome(text):
    # Remove spaces and convert to lowercase
    processed_text = text.replace(" ", "").lower()

    # Check if the processed text is equal to its reverse
    if processed_text == processed_text[::-1]:
        return True
    else:
        return False

user_text = input("Enter some text: ")

if not user_text:
    print("Empty string. Please provide some text.")
else:
    if palindrome(user_text):
        print("This is a palindrome.")
    else:
        print("This is not a palindrome.")
