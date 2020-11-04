import pygame
pygame.init() #first command
print()
length= int(input('how wide do you want the window to be (put in pixels ex:800) '))
width= int(input('how tall do you want the window to be (put in pixels ex:600) '))
red = int(input('how much red do you want in the window (will be put in RGB format) '))
green = int(input('how much green do you want in the window (will be put in RGB format) '))
blue = int(input('how much blue do you want in the window (will be put in RGB format) '))
screen = pygame.display.set_mode((length,width)) #this is a tuple
screen.fill((red,green,blue)) #select color of background 0-255
pygame.display.flip() #update screen quickly also use .update
pygame.display.set_caption("Custum Screen") #title for the window
run = True
while run == True:
    pygame.time.delay(100)
    screen.fill((red,green,blue))
    pygame.display.update()
    for x in pygame.event.get():
        print(x)
        if x.type == pygame.QUIT:
            run = False
pygame.time.delay(50)
pygame.quit()
