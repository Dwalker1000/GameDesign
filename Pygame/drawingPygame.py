import pygame
pygame.init()
#background pick should be size of Screen
# filePath = pathlib.Path(Users\walkerd24\github\GameDesign\Unit 1\).parent
background = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Unit 1\\BackGround4.jpg")
tempSprite = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Unit 1\\pika.png")
WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
white = [0,0,0]
black = [255,255,255]

# control vars
running = True
x = 52
y = 456
w = 64
h = 62
jump = False
high = 10
def redrawWindow():
    screen.blit(background, (0,0))
    screen.blit(tempSprite, (x,y))
    pygame.display.update()

while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
    pygame.time.delay(100)
    #moving our rectangle
    KeyPress=pygame.key.get_pressed()
    #check what key was get_pressed
    speed = 10
    if KeyPress[pygame.K_LEFT] and x > speed: #subtract from x
        x -= speed
    if KeyPress[pygame.K_RIGHT] and x < WIDTH - w - speed: #Add to x
        x += speed
    if not(jump): # moving y without jump
        if KeyPress[pygame.K_SPACE]:
            jump = True
    else:
        if high >=-10:
            y -= (high*abs(high)) /2
            high -= 1
        else:
            high = 10
            jump = False
    redrawWindow()
pygame.quit()
