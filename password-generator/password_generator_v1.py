import random

# ask user for desired password length
length = int(input("enter password length: "))

# pool of characters used to generate password
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

# empty string to build password
password = ""

# generate password character by character
for i in range(length):
    password += random.choice(characters)

# display final generated password
print("your password is:", password)
