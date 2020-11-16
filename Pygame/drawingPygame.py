import pygame
pygame.init()
#background pick should be size of Screen
background = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Pygame\\Backgrounds\\BackGround4.jpg")
walkRight = [pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Pygame\\sprites\\pika.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Pygame\\sprites\\dht11.jpg")]
walkLeft = [pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Pygame\\sprites\\jumping motion.PNG"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Pygame\\sprites\\BackGround1.jpg")]
character = [pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Pygame\\sprites\\pika.png")]
WIDTH = 1000 # screen width
HEIGHT = 800 # screen height
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# control vars
running = True
x = 52 #where character starts
y = 456 #where character starts
w = 64 #width of character X
h = 62 #height of character Y
jump = False
high = 10 #height of jump
# to control the frames
clock = pygame.time.Clock()
#control left and right move
left = False
right = False
#control list
walkCount = 0
SpriteFrames = 6 #each picture is about 3 frames and we have X pictures 3*x = number (27 in this case 3*9)

def redrawWindow():
    global walkCount
    screen.blit(background, (0,0))

    if walkCount + 1 >= SpriteFrames:
        walkCount = 0

    if left:
        screen.blit(walkLeft[walkCount//3],(x,y))
        walkCount += 1

    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount +=1

    else:
        screen.blit(character, (x,y))
        walkCount = 0

    screen.blit(tempSprite, (x,y))
    pygame.display.update()

while running:
    clock.tick(SpriteFrames)
    for i in pygame.event.get():
        if i.type == pygame.QUIT: #quit sequence
            running = False
    pygame.time.delay(100)
    #moving our rectangle
    KeyPress=pygame.key.get_pressed()
    #check what key was get_pressed
    speed = 10
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
        if KeyPress[pygame.K_UP] and y > speed: #Subtract from y (optional up movement)
            y -= speed
        if KeyPress[pygame.K_DOWN] and x < HEIGHT - h - speed: # add to y (optional donwnmovement)
            y += speed
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
