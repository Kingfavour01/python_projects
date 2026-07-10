import string
import random

chars = string.digits + string.ascii_letters + string.punctuation + string.octdigits

chars = list(chars)
key = chars.copy()
random.shuffle(key)

plain_text = input("enter your message to encrypt: ")
cipher_text =""



for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
print(f"original message text is: {plain_text}")
print(f"cipher text is: {cipher_text}")


cipher_text = input("enter your message to encrypt: ")
plain_text =""



for letter in cipher_text:
    index =key.index(letter)
    plain_text += chars[index]

print(f"deciphered text is: {plain_text}")
