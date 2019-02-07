#lab13.py
"""
Write a program that prompts the user for a string, and encodes it with ROT13.
For each character, find the corresponding character, add it to an output string.
Notice that there are 26 letters in the English language, so encryption is the same as decryption.
"""
##Using the ASCII range 97-123 and chr/ord.

#Encryption
def encryptString(inputString):
    encryptedString = ""
    for c in inputString:
        encryptedString += chr(97+(ord(c)-97+13)-26)
    return encryptedString

#Decryption
def decryptString(inputString):
    decryptedString = ""
    for c in inputString:
        decryptedString += chr(((ord(c)+13)-97)+97)
    return decryptedString

inputString = input("Enter a string for encryption: ")
encryptedString = ""
rotAmt = 13

encryptedString = encryptString(inputString)

print(f"Encrypted String: {encryptedString}")

decryptedString = decryptString(encryptedString)

print(f"Decrypted String: {decryptedString}")
