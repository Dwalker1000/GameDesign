import pygame
pygame.init()
#background pick should be size of Screen
# tempSprite = pygame.image.load('character')
# backdrop = pygame.image.load('Background.png')
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH,HEIGHT))
white = [0,0,0]
black = [255,255,255]
screen.fill(white)
running = True
# control vars
x = 52
y = 572
w = 64
h = 64
r = 50
jump = False
high = 10
def redrawWindow():
    # screen.blit(tempSprite, (x,y))
    # screen.blit(backdrop, (0,0))
                    #window   color      x y w h poss where rectange starts
    pygame.draw.rect(screen,(10,123,10),(x,y,w,h))
    pygame.display.update()
                       #window   color       position     rad thick
    # pygame.draw.circle(screen,(0,120,129), (x+100,y+100),r,4) draws circle
    pygame.display.update()

while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    pygame.time.delay(100)
    #moving our rectangle
    KeyPress=pygame.key.get_pressed()
    #check what key was get_pressed
    speed = 10
    if KeyPress[pygame.K_w]:
        h += speed
    if KeyPress[pygame.K_a]:
        w -= speed
    if KeyPress[pygame.K_s]:
        h -= speed
    if KeyPress[pygame.K_d]:
        w += speed
    if KeyPress[pygame.K_LEFT] and x > speed: #subtract from x
        x -= speed
        r -= speed
    if KeyPress[pygame.K_RIGHT] and x < WIDTH - w - speed: #Add to x
        x += speed
        r += speed
    if KeyPress[pygame.K_SPACE]:
        jump = true
    if KeyPress[pygame.K_UP] and y > speed: #Subtract from y
        y -= speed
    if KeyPress[pygame.K_DOWN] and x < HEIGHT - h - speed: # add to y
        y += speed
    redrawWindow()
pygame.quit()
