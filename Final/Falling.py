import pygame
pygame.init()
#imports
walkRight = [pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight1.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight2.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight3.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight4.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight5.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight6.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight7.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight8.png")]
walkLeft = [pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft1.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft2.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft3.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft4.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft5.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft6.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft7.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft8.png")]
jumpRight = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\JumpRight.png")
jumpLeft = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\JumpLeft.png")
characterRight = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\StandingRight.png")
characterLeft = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\StandingLeft.png")
WIDTH = 800 # screen width
HEIGHT = 800 # screen height
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# control vars
running = True
x = 52 #where character starts disance from left wall
y = 456 #where character starts distance from top
w = 64 #width of character X
h = 64 #height of character Y

#jump code/walk
jump = False
high = 10 #height of jump
speed = 25 #needs to be able to be devided by 500 cleanly or will mess up on far side

# to control the frames
clock = pygame.time.Clock()

#control left and right move
left = False
right = False
true = False

#control list
walkCount = 0
SpriteFrames = 24 # number of pictures for each movement times 3
Left = False #sets default side facing the right

def redrawWindow():
    KeyPress=pygame.key.get_pressed()
    global walkCount
    global x
    global speed
    global true
    global jump
    global jumpRight
    global jumpLeft
    global Left

    #sprite movement code
    screen.fill((255,255,255))
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

while running:
    clock.tick(SpriteFrames)
    for i in pygame.event.get():
        if i.type == pygame.QUIT: #quit sequence
            running = False
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
    redrawWindow()
pygame.quit()
