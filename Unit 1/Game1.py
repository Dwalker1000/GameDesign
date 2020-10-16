import random
import time

name=input("What is your name? ")
print("Good luck! ", name)
gameWords=['python', 'java','PHP','javaScript', 'computer', 'geeks', 'keyboard','laptop', 'headphone', 'hardware','software' ]
# use the choice method of my random fucntion to pick a gameWords
answer=input('do you want to guess a word ')

while answer == 'yes':
    word= random.choice(gameWords)
    guesses =''
    turns=10
    while turns>0:
        for char in word:
            if char in guesses:
                print(char)
            else:
                print('_')
        guess= input("give me a letter: ")
        guesses += guess
        turns-=1

    answer=input('do you want to play again ')
time.sleep(5)
