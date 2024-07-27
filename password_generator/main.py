import random
import string

len = int(input("Enter password length: "))
char_values = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(len):
    password += random.choice(char_values)

print(f"Password: {password}")