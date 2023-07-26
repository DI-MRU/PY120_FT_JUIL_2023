# Instructions
# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

# For example, with a left shift of 3 –> D would be replaced by A,
# –> E would become B, and so on.

# The method is named after Julius Caesar, who used it in his private correspondence.

# Create a python program that encrypts and decrypts messages with ceasar cypher.
# The user enters the program, and then the program asks him if he wants to encrypt or decrypt, and then execute encryption/decryption on a given message and a given shift.


# method 1
# Prompt the user to choose encryption ('E') or decryption ('D')
choice = input("Enter 'E' to encrypt or 'D' to decrypt: ")

# Get the message and shift value from the user
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

# Perform encryption if the choice is 'E'
if choice.lower() == 'e':
    cipher_text = ""
    for letter in message:
        if letter.isalpha():  # Check if the character is an alphabetic letter
            ascii_offset = 65 if letter.isupper() else 97  # Determine the ASCII offset based on letter case
            encrypted_letter = chr((ord(letter) - ascii_offset + shift) % 26 + ascii_offset)
            # Perform Caesar cipher encryption: shift the letter by the given shift value
            # Wrap around within the range of alphabetic characters (26 letters)
            cipher_text += encrypted_letter
        else:
            cipher_text += letter  # Append non-alphabetic characters as is
    print("Encrypted message:", cipher_text)

# Perform decryption if the choice is 'D'
elif choice.lower() == 'd':
    decrypted_message = ""
    for letter in message:
        if letter.isalpha():  # Check if the character is an alphabetic letter
            ascii_offset = 65 if letter.isupper() else 97  # Determine the ASCII offset based on letter case
            decrypted_letter = chr((ord(letter) - ascii_offset - shift) % 26 + ascii_offset)
            # Perform Caesar cipher decryption: shift the letter back by the given shift value
            # Wrap around within the range of alphabetic characters (26 letters)
            decrypted_message += decrypted_letter
        else:
            decrypted_message += letter  # Append non-alphabetic characters as is
    print("Decrypted message:", decrypted_message)

# Handle invalid choice
else:
    print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")





# method 2
# def encrypt(message, shift):
#     cipher_text = ""
#     for letter in message:
#         if letter.isalpha():
#             ascii_offset = 65 if letter.isupper() else 97
#             encrypted_letter = chr((ord(letter) - ascii_offset + shift) % 26 + ascii_offset)
#             cipher_text += encrypted_letter
#         else:
#             cipher_text += letter
#     return cipher_text


# def decrypt(cipher_text, shift):
#     decrypted_message = ""
#     for letter in cipher_text:
#         if letter.isalpha():
#             ascii_offset = 65 if letter.isupper() else 97
#             decrypted_letter = chr((ord(letter) - ascii_offset - shift) % 26 + ascii_offset)
#             decrypted_message += decrypted_letter
#         else:
#             decrypted_message += letter
#     return decrypted_message


# def main():
#     choice = input("Enter 'E' to encrypt or 'D' to decrypt: ")
#     message = input("Enter the message: ")
#     shift = int(input("Enter the shift value: "))

#     if choice.lower() == 'e':
#         encrypted_message = encrypt(message, shift)
#         print("Encrypted message:", encrypted_message)
#     elif choice.lower() == 'd':
#         decrypted_message = decrypt(message, shift)
#         print("Decrypted message:", decrypted_message)
#     else:
#         print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")


# if __name__ == '__main__':
#     main()



