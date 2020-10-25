import random
import time
print("***************************************************")
print("*                  Randome Words                  *")
print("*                                                 *")
print("*     Instructions: A word will be randomely      *")
print("*     selected from a list. That word will be     *")
print("*  scrambled. your job is to unscramble the word. *")
print("*          guess the word in order to win.        *")
print("*                                                 *")
print("*  pick a word set                                *")
print("*  1. random                                      *")
print("*  2. computer science                            *")
print("*  3. exit Game                                   *")
print("***************************************************")
start = input("(1,2,3) ")
while start == '1':
    name=input("What is your name? ")
    print("Good luck!", name)
    gameWords = ['potato', 'bagel', 'aardvark', 'unicorn', 'doppelganger', 'agenda', 'bubbles', 'Whirlpool', 'bacon', 'husky', 'pineapple', 'flamingo', 'rubber', 'dubstep']
    word= random.choice(gameWords)
    mix = random.sample(word,len(word))
    print(mix)
    guesses =''
    final = ''
    while word not in final:
        for char in word:
            if char in guesses:
                print(char,end = '')
                final = final+char
            else:
                print('_', end = ' ')
        print('')
        if word in guesses:
            print ("congrats you guessed the word")
            start = ''
            break
        guess= input("guess the next letter: ")
        guesses += guess.lower()
