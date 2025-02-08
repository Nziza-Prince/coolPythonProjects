import random
import string

def generatePass(pass_length,include_uppercase,include_specialChars,include_digits):
    if(pass_length < include_digits+include_specialChars+include_uppercase):
        raise ValueError
    
    password = ''
    if(include_digits):
        password+=random.choice(string.digits)
    if(include_specialChars):
        password+=random.choice(string.punctuation)
    if(include_uppercase):
        password+=random.choice(string.ascii_uppercase)
        
    characters = string.ascii_lowercase
    if(include_specialChars):
        characters+=string.punctuation
    if(include_digits):
        characters+=string.digits
    if(include_uppercase):
        characters+=string.ascii_uppercase
        
    for _ in range(pass_length - len(password)):
        password+=random.choice(characters)
        
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

def main():
    pass_length = int(input("Enter the required length: "))
    include_uppercase = input("Include Uppercase letters(y/n)").lower().strip() == 'y'
    include_specialChars= input("Include Special characters(y/n)").lower().strip() == 'y'
    include_digits= input("Include digits(y/n)").lower().strip() == 'y'
    try:
        password = generatePass(pass_length,include_uppercase,include_specialChars,include_digits)
        print(password)
    except ValueError as e:
        print(e)
    
if __name__ == '__main__':
    main()
    