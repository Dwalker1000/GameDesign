import pygame
import os
pygame.init()
#background pick should be size of Screen
tempSprite = pygame.image.load('dht11.jpg')
background = pygame.image.load('Background.png')
WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
white = [0,0,0]
black = [255,255,255]

# control vars
running = True
x = 52
y = 572
w = 64
h = 62
jump = False
high = 10
def redrawWindow():
    screen.blit(tempSprite, (x,y))
    screen.blit(backdrop, (0,0))
    # screen.fill((black))
    # pygame.draw.rect(screen,(10,123,10),(x,y,w,h))
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
        if KeyPress[pygame.K_UP] and y > speed: #Subtract from y
            y -= speed
        if KeyPress[pygame.K_DOWN] and x < HEIGHT - h - speed: # add to y
            y += speed
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
