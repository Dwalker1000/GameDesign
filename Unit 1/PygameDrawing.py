import pygame
pygame.init()
screenx = 800
screeny = 800
screen = pygame.display.set_mode((800,800))
white = [0,0,0]
black = [255,255,255]
screen.fill(white)
running = True
# control vars
x1=200
y1=200
w1=50
h1=100
r = 50
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    pygame.time.delay(100)
    #moving our rectangle
    rectangeSpeed=pygame.key.get_pressed()
    #check what key was get_pressed
    speed = 10
    if rectangeSpeed[pygame.K_w]:
        h1 += speed
    if rectangeSpeed[pygame.K_a]:
        w1 -= speed
    if rectangeSpeed[pygame.K_s]:
        h1 -= speed
    if rectangeSpeed[pygame.K_d]:
        w1 += speed
    if rectangeSpeed[pygame.K_LEFT]: #subtract from x
        x1 -= speed
        r -= speed
    if rectangeSpeed[pygame.K_RIGHT]: #Add to x
        x1 += speed
        r += speed
    if rectangeSpeed[pygame.K_UP]: #Subtract from y
        y1 -= speed
    if rectangeSpeed[pygame.K_DOWN]: # add to y
        y1 += speed
    #                window   color      x y w h poss where rectange starts
    screen.fill(white)
    pygame.draw.rect(screen,(10,123,10),(x1,y1,w1,h1))
    pygame.display.update()
    #                  window   color       position     rad thick
    pygame.draw.circle(screen,(0,120,129), (x1+100,y1+100),r,4)
    pygame.display.update()
pygame.quit()
