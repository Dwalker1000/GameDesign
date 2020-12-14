import pygame, sys

pygame.init()
WIDTH = 1000 # screen width
HEIGHT = 800 # screen height
screen = pygame.display.set_mode((WIDTH,HEIGHT))

base_font = pygame.font.Font(None,24)
user_text = ''

nameInputBool = True
while nameInputBool == True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                if event.key == pygame.K_RETURN:
                    nameInputBool = False
                else:
                    user_text += event.unicode

    input_rect = pygame.Rect(30,30,140,32)
    pygame.draw.rect(screen,(255,255,255),input_rect,2)

    title_surface = base_font.render("enter your name",True,(255,255,255))
    screen.blit(title_surface, (input_rect.x, 10))

    text_surface = base_font.render(user_text,True,(255,255,255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y +5))

    input_rect.w = max(100, text_surface.get_width() + 10)

    pygame.display.update()

    new_name = text_surface

print(text_surface)
