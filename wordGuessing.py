import random
import re
filename = './words.txt'
def displayWord(secret_word,guessed_letters):
    
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter,end='')
        else:
            print('_',end='')

def is_word_guessed(secret_word,guessed_letters):
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True

def getGuess(guessed_letters):
    while True:
        userGuess = input("\nGuess letter: ")
        if len(userGuess) != 1:
            print("Enter only one letter")
        elif userGuess in guessed_letters:
            print("Letter already guessed")
        elif not re.search('[a-z]',userGuess):
            print("Invalid guess try again!")
        else:
            return userGuess

  
def main():
    words = ['nziza','girraffe','lion','leandre','flicky ']
    # print(words)
    secret_word = random.choice(words).strip()
    print(secret_word)
    guessed_letters = []
    attempts = 6
    while attempts > 0:
        displayWord(secret_word,guessed_letters)
        print(f'\n{attempts} attempts remaining')
        userGuess = getGuess(guessed_letters)
        guessed_letters.append(userGuess)
        if userGuess in secret_word:
            print("Good guess")
            if is_word_guessed(secret_word,guessed_letters):
                print(f"Congs You guessed the word {secret_word}")
                break
        else:
            print("Wrong guess")
            attempts-=1
            if attempts == 0:
                print(f"game over the word was {secret_word}")  


if __name__ == "__main__":
    main()

