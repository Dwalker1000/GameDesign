import random
import time
name=input("What is your name? ")
print("Good luck!", name)
gameWords=['python', 'java','php','javascript', 'computer', 'geeks', 'keyboard', 'laptop', 'headphone', 'hardware','software', 'cpu', 'drivers', 'usb ports', 'binary', 'graphics', 'pixels', 'intel', 'ryzen', 'battery']
# use the choice method of my random fucntion to pick a gameWords
answer=input('do you want to guess a word? ')
while answer == 'yes':
    word= random.choice(gameWords)
    guesses =''
    final = ''
    turns=10
    while turns>0:
        for char in word:
            if char in guesses:
                print(char,end = '')
                final = final+char
            else:
                print('_', end = ' ')
        print('')
        if word in final:
            print('you win')
            print("the word is: "+ word)
            break
        guess= input("give me a letter: ")
        guesses += guess.lower()
        if guess not in word:
            turns-=1
            print("you have ",end = '')
            print(turns,end = '')
            print(" turns left",end = '')
            print()
        if turns == 10:
            print('_',end = '')
            print('  ', end = '')
            print('O',end = '')
            print('  ', end = '')
            print('_')
            print(' ',end = '')
            print('\\',end = '')
            print('/',end = '')
            print('|',end = '')
            print('\\',end = '')
            print('/')
            print('  ', end = '')
            print('/',end = '')
            print(' \  ')
        if turns == 9:
            print(' ',end = '')
            print('  ', end = '')
            print('O',end = '')
            print('  ', end = '')
            print('_')
            print(' ',end = '')
            print('\\',end = '')
            print('/',end = '')
            print('|',end = '')
            print('\\',end = '')
            print('/')
            print('  ', end = '')
            print('/',end = '')
            print(' \  ')
        if turns == 8:
            print(' ',end = '')
            print('  ', end = '')
            print('O',end = '')
            print('  ', end = '')
            print(' ')
            print(' ',end = '')
            print('\\',end = '')
            print('/',end = '')
            print('|',end = '')
            print('\\',end = '')
            print('/')
            print('  ', end = '')
            print('/',end = '')
            print(' \  ')
        if turns == 7:
            print(' ',end = '')
            print('  ', end = '')
            print('O',end = '')
            print('  ', end = '')
            print(' ')
            print(' ',end = '')
            print(' ',end = '')
            print('/',end = '')
            print('|',end = '')
            print('\\',end = '')
            print('/')
            print('  ', end = '')
            print('/',end = '')
            print(' \  ')
        if turns == 6:
            print(' ',end = '')
            print('  ', end = '')
            print('O',end = '')
            print('  ', end = '')
            print(' ')
            print(' ',end = '')
            print(' ',end = '')
            print('/',end = '')
            print('|',end = '')
            print('\\',end = '')
            print(' ')
            print('  ', end = '')
            print('/',end = '')
            print(' \  ')
        if turns == 5:
            print(' ',end = '')
            print('  ', end = '')
            print('O',end = '')
            print('  ', end = '')
            print(' ')
            print(' ',end = '')
            print(' ',end = '')
            print('/',end = '')
            print('|',end = '')
            print(' ',end = '')
            print(' ')
            print('  ', end = '')
            print('/',end = '')
            print(' \  ')
        if turns == 4:
            print(' ',end = '')
            print('  ', end = '')
            print('O',end = '')
            print('  ', end = '')
            print(' ')
            print(' ',end = '')
            print(' ',end = '')
            print(' ',end = '')
            print('|',end = '')
            print(' ',end = '')
            print(' ')
            print('  ', end = '')
            print('/',end = '')
            print(' \  ')
        if turns == 3:
            print(' ',end = '')
            print('  ', end = '')
            print('O',end = '')
            print('  ', end = '')
            print(' ')
            print(' ',end = '')
            print(' ',end = '')
            print(' ',end = '')
            print('|',end = '')
            print(' ',end = '')
            print(' ')
            print('  ', end = '')
            print(' ',end = '')
            print(' \  ')
        if turns == 2:
            print(' ',end = '')
            print('  ', end = '')
            print('O',end = '')
            print('  ', end = '')
            print(' ')
            print(' ',end = '')
            print(' ',end = '')
            print(' ',end = '')
            print('|',end = '')
            print(' ',end = '')
            print(' ')
            print('  ', end = '')
            print(' ',end = '')
            print('    ')
        if turns == 1:
            print(' ',end = '')
            print('  ', end = '')
            print('O',end = '')
            print('  ', end = '')
            print(' ')
            print(' ',end = '')
            print(' ',end = '')
            print(' ',end = '')
            print(' ',end = '')
            print(' ',end = '')
            print(' ')
            print('  ', end = '')
            print(' ',end = '')
            print('    ')
        if turns == 0:
            print('Game Over')
            break
    answer=input('do you want to play again ')
time.sleep(5)
