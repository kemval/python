def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""
    
    for char in message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_message += shifted_char
        else:
            encrypted_message += char

    return encrypted_message


def get_shift_value():
    while True:
        shift = input("Enter the shift value (1-25): ")
        if shift.isdigit():
            shift = int(shift)
            if 1 <= shift <= 25:
                return shift
            else:
                print("Invalid shift value. Please enter a value between 1 and 25.")
        else:
            print("Invalid input. Please enter a valid number.")


message = input("Enter a line of text to encrypt: ")
shift = get_shift_value()
encrypted_message = caesar_cipher_encrypt(message, shift)
print("Encrypted message:", encrypted_message)

    
        


