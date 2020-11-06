import random
import time
import os
from datetime import date
def menu ():
    print("***********************************************************")
    print("*                         Hang Man                        *")
    print("*                                                         *")
    print("*          Instructions: A word will be randomly          *")
    print("*        selected from a list. your job is to guess       *")
    print("*          the word picked from the list to win.          *")
    print("*                                                         *")
    print("*  1. play                                                *")
    print("*  2. see past scores (dont do if you havent played yet)  *")
    print("*  3. Exit Game                                           *")
    print("***********************************************************")
def start ():
    start = input("(1,2,3) ")
    return start
def play ():

    name=input("What is your name? ")
    print("Good luck!", name)
    path = "words.txt"
    ifExist = os.path.exists(path)

    f = open('words.txt', 'w')
    words = ['python', 'java', 'php', 'javascript', 'computer', 'geeks', 'keyboard', 'laptop', 'headphone', 'hardware', 'software', 'cpu', 'drivers', 'usb ports', 'binary', 'graphics', 'pixels', 'intel', 'ryzen', 'battery']
    z = len(words)
    for x in range (z):
        y = words[x]
        f.write(y+"\n")
    f.close()

    # use the choice method of my random fucntion to pick a gameWords
    answer=input('do you want to guess a word? ')
    score = 0
    while answer == 'yes':
        f = open('words.txt', 'r')
        gameWords = []
        for line in f:
            gameWords.append(line.strip())
        f.close()
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
                score = score + 1
                print("you have a score of ",end = '')
                print(score)
                answer=input('do you want to guess another word ')
                if answer == 'no':
                    path = "highscores.txt"
                    ifExist = os.path.exists(path)
                    if ifExist == True:
                        text_file = open("highscores.txt", "a")
                        score2 = str(score)
                        today = date.today()
                        text_file.write("\n" + name +"\t"+ score2 + "\t" + str(today.day())+"-"+str(today.month())+"-"+ str(today.year())+ "\n")
                    elif ifExist == False:
                        text_file = open("highscores.txt", "w")
                        score2 = str(score)
                        today = date.today()
                        text_file.write("\n" + name +"\t"+ score2 + "\t" + (today.day()+"-"+today.month()+"-"+ today.year()+ "\n")
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
                print("you ended with a score of ", end ='')
                print(score)
                answer=input('do you want to play again ')
                path = "highscores.txt"
                ifExist = os.path.exists(path)
                if ifExist == True:
                    text_file = open("highscores.txt", "a")
                    score2 = str(score)
                    today = date.today()
                    text_file.write("\n" + name +"\t"+ score2 + "\t" + today.day()+"-"+today.month()+"-"+ today.year()+ "\n")
                    text_file.close()
                elif ifExist == False:
                    text_file = open("highscores.txt", "w")
                    score2 = str(score)
                    today = date.today()
                    text_file.write("\n" + name +"\t"+ score2 + "\t" + today.day()+"-"+today.month()+"-"+ today.year()+ "\n")
                    text_file.close()
                break
def score():
    text_file = open("highscores.txt", "r")
    whole_thing = text_file.read()
    print (whole_thing)
    text_file.close()

gameWords = []
xyz = 0
while xyz == 0:
    menu()
    x = start()
    if x == '1':
        play()
    if x == '2':
        score()
        break
    if x == '3':
        print('Thanks for playing! Goodbye.')
        xyz = 1
        break
