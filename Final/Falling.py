import pygame, random, sys

# the game will have meteors falling from the sky
# if player gets hit they louse
# score will be decided based on the dificlty and ime survived
pygame.init()
#imports
walkRight = [pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight1.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight2.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight3.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight4.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight5.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight6.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight7.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight8.png")]
walkLeft = [pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft1.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft2.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft3.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft4.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft5.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft6.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft7.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft8.png")]
jumpRight = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\JumpRight.png")
jumpLeft = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\JumpLeft.png")
background = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\Background.jpg")
characterRight = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\StandingRight.png")
characterLeft = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\StandingLeft.png")
meteor = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\fireball.jpg")
Brick = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\Brick.jpg")
#screen vars
WIDTH = 1000 # screen width
HEIGHT = 800 # screen height
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# control/default vars for player
running = True
click = False
alive = True
x = 368 #where character starts disance from left wall
y = 688 #where character starts distance from top
w = 64 #width of character X
h = 64 #height of character Y

#meteor code
meteor_Size = 64
meteor_x = [random.randint(0,WIDTH-meteor_Size), 0]
meteor_y = 0

#jump code/walk
jump = False
high = 10 #height of jump
speed = 15 #needs to be able to be devided by 500 cleanly or will mess up on far side

# to control the frames
clock = pygame.time.Clock()

#control left and right move
left = False
right = False
true = False

# set up fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

#control list
walkCount = 0
SpriteFrames = 24 # number of pictures for each movement times 3
Left = False #sets default side facing the right

#dificulty
dificlty = None

#window
def redrawWindow(dificlty, alive):
    KeyPress=pygame.key.get_pressed()
    global walkCount
    global x
    global speed
    global true
    global jump
    global jumpRight
    global jumpLeft
    global Left
    global meteor

    #sprite movement rendering code
    screen.blit(background, (0,0))
    if walkCount + 1 >= SpriteFrames:
        walkCount = 0
    if left:
        Left = True
        if jump == True:
            screen.blit((jumpLeft), (x,y))
        else:
            screen.blit(walkLeft[walkCount//3],(x,y))
            walkCount += 1
    elif right:
        Left = False
        if jump == True:
            screen.blit((jumpRight), (x,y))
        else:
            screen.blit(walkRight[walkCount//3], (x,y))
            walkCount +=1
    else:
        if Left == True:
            screen.blit((characterLeft),(x,y))
            walkCount = 0
        else:
            screen.blit((characterRight),(x,y))
            walkCount = 0
    #screen update
    pygame.display.update()

#message code
def display_message(message):
    pygame.time.delay(1000)
    win.fill((255,255,255))
    text = WORD_FONT.render(message, 1, (0,0,0))
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

#menu
def menu():
    global words
    global word
    global mx
    global my
    global run
    global click

    x = True
    while x == True:
        #mouse position and white fill
        mx, my = pygame.mouse.get_pos()
        screen.fill((255,255,255))

        #buttons
        button_1 = pygame.Rect(105,295,200,50)
        button_2 = pygame.Rect(395,295,200,50)
        button_3 = pygame.Rect(695,295,200,50)
        button_4 = pygame.Rect(195,495,275,50)
        button_5 = pygame.Rect(565,495,200,50)
        pygame.draw.rect(screen, (255,0 ,0), button_1)
        pygame.draw.rect(screen, (255,0 ,0), button_2)
        pygame.draw.rect(screen, (255,0 ,0), button_3)
        pygame.draw.rect(screen, (255,0 ,0), button_4)
        pygame.draw.rect(screen, (255,0 ,0), button_5)

        #menu text
        text1 = TITLE_FONT.render("The Sky Is Falling", 1, (0,0,0))
        text2 = WORD_FONT.render("instructions", 1, (0,0,0))
        text2_0 = WORD_FONT.render("meteors will be falling from the sky", 1, (0,0,0))
        text2_1 = WORD_FONT.render("if you get hit you louse", 1, (0,0,0))
        text2_2 = WORD_FONT.render("use the left and right arow to move", 1, (0,0,0))
        text3 = WORD_FONT.render("easy", 1, (0,0,0))
        text4 = WORD_FONT.render("medium", 1, (0,0,0))
        text5 = WORD_FONT.render("hard", 1, (0,0,0))
        text6 = WORD_FONT.render("scoreboard", 1, (0,0,0))
        text7 = WORD_FONT.render("quit", 1, (0,0,0))
        #text display
        screen.blit(text1, (int(WIDTH/2 - (text1.get_width()/2)), 20))
        screen.blit(text2, (int(WIDTH/2 - text2.get_width()/2), 90))
        screen.blit(text2_0, (int(WIDTH/2 - text2_0.get_width()/2), 140))
        screen.blit(text2_1, (int(WIDTH/2 - text2_1.get_width()/2), 190))
        screen.blit(text2_2, (int(WIDTH/2 - text2_2.get_width()/2), 240))
        screen.blit (text3, (int(WIDTH/5 - text3.get_width()/2), 300))
        screen.blit(text4, (int(WIDTH/2 - text4.get_width()/2), 300))
        screen.blit(text5, (int(WIDTH/1.25 - text5.get_width()/2), 300))
        screen.blit(text6, (int(WIDTH/3 - text6.get_width()/2), 500))
        screen.blit(text7, (int(WIDTH/1.5 - text7.get_width()/2), 500))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
                break
        #if mouse left clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
        #button colision and action
        #easy
        if button_1.collidepoint((mx,my)):
            if click:
                screen.fill((0,0,0))
                dificlty = "easy"
                pygame.display.update()
                x = False
                main(dificlty)
                pass
        #normal
        if button_2.collidepoint((mx,my)):
            if click:
                screen.fill((0,0,0))
                dificlty = "normal"
                pygame.display.update()
                x = False
                main(dificlty)
                pass
        #Hard
        if button_3.collidepoint((mx,my)):
            if click:
                screen.fill((0,0,0))
                dificlty = "hard"
                pygame.display.update()
                x = False
                maindificlty
                pass
        #scoreboard
        if button_4.collidepoint((mx,my)):
            if click:
                running = False
                pass
        #quit
        if button_5.collidepoint((mx,my)):
            if click:
                running = False
                break
        click = False

#main
def main(dificlty):
    global running
    global jump
    global x
    global y
    global high
    global speed
    global Clock
    global right
    global left
    while running and alive:
        clock.tick(SpriteFrames)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
                break
        pygame.time.delay(100)
        # movement
        KeyPress=pygame.key.get_pressed()
        #check what key was get_pressed
        if KeyPress[pygame.K_LEFT] and x > speed: #subtract from x left movement
            x -= speed
            left = True
            right = False
        elif KeyPress[pygame.K_RIGHT] and x < WIDTH - w - speed: #Add to x right movement
            x += speed
            left = False
            right = True
        #reset code when not moving
        else:
            left = False
            right = False
            walkCount = 0
        #jump code
        if not(jump): # moving y without jump
            if KeyPress[pygame.K_SPACE]:
                jump = True
                left = False
                right = False
                walkCount = 0
        else:
            if high >=-10:
                y -= (high*abs(high)) /2
                high -= 1
            else:
                high = 10
                jump = False
        redrawWindow(dificlty, alive)
        meteor_1 = pygame.Rect(meteor_x,meteor_y,meteor_Size,meteor_Size)
        pygame.draw.rect(screen, (0,0,255), (meteor_1))
        pygame.display.update()
menu()
pygame.quit()
