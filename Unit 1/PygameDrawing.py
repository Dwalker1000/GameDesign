import pygame
pygame.init()
#background pick should be size of Screen
tempSprite = pygame.image.load('character')
backdrop=pygame.image.load('Background.png')
WIDTH = 800
HEIGHT = 607
screen = pygame.display.set_mode((WIDTH,HEIGHT))
white = [0,0,0]
black = [255,255,255]
screen.fill(white)
running = True
# control vars
x=200
y=200
w=50
h=100
r = 50
hbox = 200
wbox = 200
rect = pygame.Rect(x,y,hbox,wbox)

while running:
    screen.blit(backdrop, (0,0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    pygame.time.delay(100)
    #moving our rectangle
    rectangeSpeed=pygame.key.get_pressed()
    #check what key was get_pressed
    speed = 10
    if rectangeSpeed[pygame.K_w]:
        h += speed
    if rectangeSpeed[pygame.K_a]:
        w -= speed
    if rectangeSpeed[pygame.K_s]:
        h -= speed
    if rectangeSpeed[pygame.K_d]:
        w += speed
    if rectangeSpeed[pygame.K_LEFT] and x > speed: #subtract from x
        x -= speed
        r -= speed
    if rectangeSpeed[pygame.K_RIGHT] and x < WIDTH - w - speed: #Add to x
        x += speed
        r += speed
    if rectangeSpeed[pygame.K_UP] and y > speed: #Subtract from y
        y -= speed
    if rectangeSpeed[pygame.K_DOWN] and x < HEIGHT - h - speed: # add to y
        y += speed
    screen.blit(tempSprite, (x,y))
    #                window   color      x y w h poss where rectange starts
    # pygame.draw.rect(screen,(10,123,10),(x,y,w,h))
    # pygame.display.update()
    #                  window   color       position     rad thick
    # pygame.draw.circle(screen,(0,120,129), (x+100,y+100),r,4)
    # pygame.display.update()
pygame.quit()
