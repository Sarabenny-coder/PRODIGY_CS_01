def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.isupper():
                result += chr((shifted - 65) % 26 + 65)
            else:
                result += chr((shifted - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Input from user
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print(f"Encrypted message: {encrypted}")
print(f"Decrypted message: {decrypted}")
