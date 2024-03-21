# 2. User Input Data Processor
# Objective:
# The aim of this assignment is to process and for mat user input data.

# Task 1:

# Task 2:

# Task 3: Email Formatter
# Implement a script that ensures all user email addresses are in a standard format
first_name=input("Pleace introduce your firstname")
last_name=input("Pleace introduce your lastname")

if len(first_name)>=2 and len(last_name)>=2:
    print("Your first name and last name are longh enough")
else:
    print("Your first name and last name should be longer than 2 characters")

passw = input("Please introduce a password ")

def check(password):
    if len(password) > 8 and any(char.islower() for char in password) and any(char.isupper() for char in password) and any(char.isdigit() for char in password):
        print("Valid format")
    else:
        print("Should be at least 8 characters, upper case, lower case and a number")

check(passw)

import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
email=input("Please introduce a valid email")
def checker(email):
    if re.fullmatch(regex, email):
      print("Valid email")
    else:
      print("Invalid email, this should be the format user@mail.com")

checker(email)
      
