import pygame
#drawing with python
pygame.init() #first command
screen = pygame.display.set_mode((1280,800)) #this is a tuple
screen.fill((0,0,0)) #select color of background 0-255
pygame.display.flip() #update screen quickly also use .update
pygame.display.set_caption("Testing pygame") #title for the window
run = True
while run == True:
    pygame.time.delay(100)
    screen.fill((162,39,142))
    pygame.display.update()
    for x in pygame.event.get():
        print(x)
        if x.type == pygame.QUIT:
            run = False
pygame.time.delay(50)
pygame.quit()
