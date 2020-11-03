import random
import time
import os
def menu ():
    print("***************************************************")
    print("*                    Hang Man                     *")
    print("*                                                 *")
    print("*      Instructions: A word will be randomly      *")
    print("*    selected from a list. your job is to guess   *")
    print("*      the word picked from the list to win.      *")
    print("*                                                 *")
    print("*  1. play                                        *")
    print("*  2. see past scores                             *")
    print("*  3. Exit Game                                   *")
    print("***************************************************")
def start ():
    start = input("(1,2,3) ")
    return start
def play ():
    global gameWords
    name=input("What is your name? ")
    print("Good luck!", name)

    path = "words.txt"
    ifExist = os.path.exists(path)
    if ifExist == "True":
        f = open('words.txt', 'r')
        gameWords = []
        for line in f:
            gameWords.append(line.strip())
        f.close()
        return gameWords
    elif ifExist == "False":
        f = open('words.txt', 'w')
        gameWords = ['python', 'java', 'php', 'javascript', 'computer', 'geeks', 'keyboard', 'laptop', 'headphone', 'hardware', 'software', 'cpu', 'drivers', 'usb ports', 'binary', 'graphics', 'pixels', 'intel', 'ryzen', 'battery']
        f.write(gameWords)
        f.close()
        return gameWords

    # use the choice method of my random fucntion to pick a gameWords
    answer=input('do you want to guess a word? ')
    while answer == 'yes':
        word= random.choice(gameWords)
        guesses =''
        final = ''
        score = 0
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
                score += 1
                print("you have a score of "+ score)
                answer=input('do you want to keep playing ')
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
                answer=input('do you want to play again ')
                break
            path = "highscores.txt"
            ifExist = os.path.exists(path)
            if ifExist == "True":
                text_file = open("highscores.txt", "a")
                text_file.write("\n" + name + ' has a score of ' + score + "\n")
                text_file.close()
            elif ifExist == "False":
                text_file = open("highscores.txt", "w")
                text_file.write("\n" + name + ' has a score of ' + score + "\n")
                text_file.close()

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
    while x == '1':
        play()
    while x == '2':
        score()
        break
    if x == '3':
        print('Thanks for playing! Goodbye.')
        break
