import pygame
pygame.init()
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Pygame\\sprites\\pika.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Pygame\\sprites\\dht11.jpg")]
walkLeft = [pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Pygame\\sprites\\jumping motion.PNG"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Pygame\\sprites\\BackGround1.jpg")]
bg = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Pygame\\Backgrounds\\BackGround4.jpg")
character = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Pygame\\sprites\\pika.png")

x = 50
y = 400
width = 40
height = 60
speed = 5
#to control the frames
clock = pygame.time.Clock()

Jump = False
high = 10
#control left and right move
left = False
right = False
#control my list
walkCount = 0

def redrawGameWindow():
    global walkCount #it makes sure is using the global walkCount that created earlier

    screen.blit(bg, (0,0))
    if walkCount + 1 >= 6:
        walkCount = 0
    if left:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        screen.blit(character, (x, y))
        walkCount = 0
    pygame.display.update()

run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < WIDTH - speed - width:
        x += speed
        left = False
        right = True

    else:
        left = False
        right = False
        walkCount = 0

    if not(Jump):
        if keys[pygame.K_UP] and y > speed:     # I need to substract to the y
            y -= speed
        if keys[pygame.K_DOWN] and y < HEIGHT - height - speed:    # I need to add to the y
            y += speed
        if keys[pygame.K_SPACE]:
            Jump = True
            left = False
            right = False
            walkCount = 0
    else:
        if high >= -10:
            y -= (high * abs(high)) * 0.5
            high -= 1
        else:
            high = 10
            Jump = False

    redrawGameWindow()

pygame.quit()
