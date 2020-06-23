#!/usr/bin/python3

import random
characters = 'abcdefghijklmnopqrstuvwxyz0123456789!#-?@*_$%&().+=/\ABCDEFGHIJKLMNOPQRSTUVWXYZ'

password_length = int(input('Enter password length: '))
password = ''
for c in range(password_length):
   password += random.choice(characters)
print(password)
