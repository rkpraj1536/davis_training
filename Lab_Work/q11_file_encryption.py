# Question 11: File Encryption (Basic Caesar Cipher)

shift = 3

with open("input.txt", "r") as input_file:
    original_text = input_file.read()

encrypted_text = ""

for character in original_text:
    if character.isalpha():
        if character.islower():
            encrypted_text += chr((ord(character) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += chr((ord(character) - ord('A') + shift) % 26 + ord('A'))
    else:
        encrypted_text += character

with open("encrypted.txt", "w") as encrypted_file:
    encrypted_file.write(encrypted_text)

print("File encrypted successfully")
