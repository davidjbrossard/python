import math as m

"""
This method takes in a string and returns another string. It encrypts the content of the string by using the Caesar cipher.
"""
def encrypt(message, offset):
    encryptedString = "";
    for a in message:
        encryptedString+=chr(ord(a)+offset);
    return encryptedString;

"""
This method takes in a string and returns another string. It decrypts the content of the string by using the inverse of the Caesar cipher
"""
def decrypt(message,offset):
    decryptedString = "";
    for a in message:
        decryptedString+=chr(ord(a)-offset);
    return decryptedString;

print(encrypt("Zebulon", 1));
print(decrypt(encrypt("Zebulon", 1),1));