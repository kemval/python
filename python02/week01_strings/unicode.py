def encrypt(message, key):
    encrypted_list = []
    for char in message:
        encrypted_value = ord(char) ^ key
        encrypted_list.append(encrypted_value)
    return encrypted_list

def decrypt(encrypted_list, key):
    decrypted_message = ''
    for encrypted_value in encrypted_list:
        decrypted_char = chr(encrypted_value ^ key)
        decrypted_message += decrypted_char
    return decrypted_message

message = input('Enter a line of text: ')
encryption_key = (42*10)-5

encrypted_list = encrypt(message, encryption_key)
print("Encrypted list:", encrypted_list)

decrypted_message = decrypt(encrypted_list, encryption_key)
print("Decrypted message:", decrypted_message)