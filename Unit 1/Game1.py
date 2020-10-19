import random
import time

name=input("What is your name? ")
print("Good luck! ", name)
gameWords=['python', 'java','php','javascript', 'computer', 'geeks', 'keyboard', 'laptop', 'headphone', 'hardware','software', 'cpu', 'drivers', 'usb ports']
# use the choice method of my random fucntion to pick a gameWords
answer=input('do you want to guess a word ')
print('only guess lower case letters')
while answer == 'yes':
    word= random.choice(gameWords)
    guesses =''
    turns=10
    while turns>0:
        for char in word:
            if char in guesses:
                print(char,end = '')
            else:
                print('_', end = ' ')
        print('')
        guess= input("give me a letter: ")
        if guess in word:
            break
        else:
            turns-=1
        guesses += guess
        print(turns)

        if turns == 0:
            print('Game Over')
    answer=input('do you want to play again ')
time.sleep(5)
