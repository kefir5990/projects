import random
import string

chars = string.ascii_letters + string.digits + " " 
list_default = list(chars)

keys = list(chars)
random.shuffle(keys)

user_input = input("Write down your sentence: ")
result = ""

for letter in user_input:
    index = list_default.index(letter)
    result += keys[index]

print(f"Your input: {user_input}")
print(f"Encryption result: {result}")
