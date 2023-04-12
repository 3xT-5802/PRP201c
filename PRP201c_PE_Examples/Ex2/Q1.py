#A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
#   1. At least 1 letter between [a-z]
#   2. At least 1 number between [0-9]
#   1. At least 1 letter between [A-Z]
#   3. At least 1 character from [$#@]
#   4. Minimum lenth of transaction password: 6
#   5. Maximum lenth of transaction password: 12
#Your program should accept a sequence of comma separated passwords
# and will check them according to the above criteria.
# Passwords that match the criteria are to be printed, each separated by a comma.

import re

# Input username and password
while True:
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
    if (username_input == '' or password_input == '' ):
        print("Username and Password cannot be blank!\n")
        continue
    break

# Make a list if there are more than 1 password
password_list = password_input.strip().split(',')
valid_pass_list = list()
for password in password_list:
    # Set validating parameters
    lower = False
    digit = False
    upper = False
    spec_char = False
    length = False
    # Validate each password, based on validating conditions
    password = password.strip()
    password_size = len(password)
    if re.search('.*[a-z]+.*', password):
        lower = True
    if re.search('.*[0-9]+.*', password):
        digit = True
    if re.search('.*[A-Z]+.*', password):
        upper = True
    if re.search('.*[$#@]+.*', password):
        spec_char = True
    if password_size >= 6 and password_size <= 12:
        length = True
    if lower and digit and upper and spec_char and length:
        valid_pass_list.append(password)

# Print valid passwords
if len(valid_pass_list) > 0:
    print("Valid passwords: ", end = '')
    for i in range(len(valid_pass_list) - 1):
        print(valid_pass_list[i], end = ', ')
    print(valid_pass_list[len(valid_pass_list) - 1]) # Print the last password in the list
else:
    print("All passwords are invalid.")