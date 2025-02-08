import re

def checkPass(password):
    strength = 0
    if len(password) >= 8:
        strength+=1
    if re.search('[a,z]',password):
        strength+=1
    if(re.search('[A-Z]',password)):
        strength+=1
    if re.search('[!@#$%^&*()+_-~`]',password):
        strength+=1
    if re.search('[0-9]',password):
        strength+=1
        
    return strength
        
def main():
    password = input("Enter password to check: ")
    strength = checkPass(password)
    if strength <=1 :
        print("Password is Very Weak")
        
    if strength == 2 :
        print("Password is Weak")
        
    if strength == 3 :
        print("Password is  Medium")
        
    if strength == 4  :
        print("Password is Strong")
        
    if strength == 5 :
        print("Password is Very Stromg")
        
if __name__ == '__main__':
    main()