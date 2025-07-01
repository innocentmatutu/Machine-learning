import re
import secrets
import string


def password_generator(length,nums,uppercase,lowercase,special_chars):
 
    #Define possible characters of a password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    #Combine all the possible characters of a passoword
    combination_characters = letters + digits + symbols

    while True:
        password = ''
        #Generate a random password
        for _ in range(length):
            password += secrets.choice(combination_characters)
             
        #Constraints on the password
        constraints = [
            (nums, r'[0-9]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]'),
            (special_chars, fr'[{symbols}]')
        ]
        #check constraints on generated password
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint,pattern in constraints
        ):
            break

    return password
    
def main():
    new_password = password_generator(12, 1, 1, 1, 1)
    print('Generated password is:', new_password)
main()