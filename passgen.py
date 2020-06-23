#!/usr/bin/python3

import random,string
characters=string.ascii_lowercase+string.ascii_uppercase+string.digits+"!#-?@*_\~<>{}$%&().+=/"

password_length = int(input('Enter password length: '))
password = ''
for c in range(password_length):
   password += random.choice(characters)
print(password)
