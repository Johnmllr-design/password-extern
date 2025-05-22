# a file to implement the password checker program for the string portion of the externship
import string

password = input("what is your new password: ")     # get a potential password from the user

# save the number of chars for each type
lower = 0
upper = 0
special = 0
numerical = 0

# check each char in the password
for char in password:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        numerical += 1
    elif char in string.punctuation:
        special += 1

if lower > 0 and upper > 0 and special > 0 and numerical > 0 and len(password) >= 8:
    print("your password is super strong!")                         # good password

else:
    error_message = ""
    # check password length
    if len(password) < 8:
        error_message = "your password needs to be at least 8 characters long"
        print(error_message)            # print the error message

    else:
        error_message = "your password needs at least one "

        # handle each password defficiencies
        if lower == 0:
            error_message += "lowercase character, "
        if upper == 0:
            error_message += "uppercase character, "
        if special == 0:
            error_message += "special character, "
        if numerical == 0:
            error_message += "numerical character, "

        print(error_message[0:len(error_message) - 2])        # print the error message
    



