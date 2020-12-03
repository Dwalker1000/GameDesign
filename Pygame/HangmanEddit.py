#Daniel walker
# import correct photos
# fix window
# create menu
#   options: 3 lvels (easy, medium, hard)
#create file for records
import pygame
import math
import random

# setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# setup  button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# set up fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# load images.
images = []
for i in range(7):
    image = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Pygame\\Hangman sprites\\hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 0
guessed = []
start = False
click = False
run = True

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)


def draw(word):
    win.fill(WHITE)

    # draw title
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20)) # Notice centering

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def menu():
    global words
    global word
    global m_x
    global m_y
    global run

    while True:
        button_1 = pygame.Rect(65,295,200,50)
        button_2 = pygame.Rect(300,295,200,50)
        button_3 = pygame.Rect(545,295,200,50)
        mx, my = pygame.mouse.get_pos()
        win.fill(WHITE)
        pygame.draw.rect(win, (255,0 ,0), button_1)
        pygame.draw.rect(win, (255,0 ,0), button_2)
        pygame.draw.rect(win, (255,0 ,0), button_3)
        text1 = TITLE_FONT.render("HANGMAN", 1, BLACK)
        win.blit(text1, (int(WIDTH/2 - (text1.get_width()/2)), 20))
        text2 = WORD_FONT.render("instructions", 1, BLACK)
        win.blit(text2, (int(WIDTH/2 - text2.get_width()/2), 90))
        text2_0 = WORD_FONT.render("try to guess a word. if you get one", 1, BLACK)
        win.blit(text2_0, (int(WIDTH/2 - text2_0.get_width()/2), 140))
        text2_1 = WORD_FONT.render("wrong then a boddy peice gets added.", 1, BLACK)
        win.blit(text2_1, (int(WIDTH/2 - text2_1.get_width()/2), 190))
        text2_2 = WORD_FONT.render(" if all peices are added then you louse.", 1, BLACK)
        win.blit(text2_2, (int(WIDTH/2 - text2_2.get_width()/2), 240))
        text3 = WORD_FONT.render("easy", 1, BLACK)
        win.blit (text3, (int(WIDTH/5 - text3.get_width()/2), 300))
        text4 = WORD_FONT.render("medium", 1, BLACK)
        win.blit(text4, (int(WIDTH/2 - text4.get_width()/2), 300))
        text5 = WORD_FONT.render("hard", 1, BLACK)
        win.blit(text5, (int(WIDTH/1.25 - text5.get_width()/2), 300))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
        if button_1.collidepoint((mx,my)):
            if click:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        break
                words = ["IDE", "REPLIT", "PYTHON", "PYGAME"]
                word = random.choice(words)
                main(word)
                pass
        if button_2.collidepoint((mx,my)):
            if click:
                words = ["JAVASCRIPT", "MOUNT", "COLLIDE", "SCANNER"]
                word = random.choice(words)
                main(word)
                pass
        if button_3.collidepoint((mx,my)):
            if click:
                words = ["COLLIDEPOINT", "", "PYTHON", "PYGAME"]
                word = random.choice(words)
                main(word)
                pass
        click = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.type == 1:
                click = True
                #     words = ["IDE", "REPLIT", "PYTHON", "PYGAME"]
                #     word = random.choice(words)

def main(word):

    global hangman_status
    global win

    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        draw(word)
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1

        draw(word)

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            display_message("You WON!")
            break

        if hangman_status == 6:
            display_message("You LOST!")
            break

while True:
    menu()
pygame.quit()
