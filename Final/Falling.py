import pygame, random, sys, os

# the game will have meteors falling from the sky
# if player gets hit they louse
# score will be decided based on the dificlty and meteors that fall off the screen
pygame.init()
#imports
walkRight = [pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight1.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight2.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight3.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight4.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight5.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight6.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight7.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkRight8.png")]
walkLeft = [pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft1.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft2.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft3.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft4.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft5.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft6.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft7.png"), pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\WalkLeft8.png")]
jumpRight = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\JumpRight.png")
jumpLeft = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\JumpLeft.png")
background = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\Background.jpg")
characterRight = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\StandingRight.png")
characterLeft = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\StandingLeft.png")
meteor = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\fireball.png")
Brick = pygame.image.load("C:\\Users\\walkerd24\\github\\GameDesign\\Final\\sprites\\Brick.jpg")
#screen vars
WIDTH = 1000 # screen width
HEIGHT = 800 # screen height
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# control/default vars for player
running = True
click = False
alive = True
player_x = 368 #where character starts disance from left wall
player_y = 688 #where character starts distance from top
player_Size = 64 #width and height of character

#meteor code
meteor_Size = 64
meteor_pos = [random.randint(0,WIDTH-meteor_Size), 0]
meteor_list = [meteor_pos]
meteor_speed = 0

#jump code/walk
jump = False
high = 10 #height of jump
speed = 15 #needs to be able to be devided by 500 cleanly or will mess up on far side

# to control the frames
clock = pygame.time.Clock()

#control left and right move
left = False
right = False
true = False

# set up fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

#control list
walkCount = 0
SpriteFrames = 24 # number of pictures for each movement times 3
Left = False #sets default side facing the right

#dificulty
dificlty = None
dificlty_multiplyer = 1
score = 0

#level SPEED
def level_speed(score,meteor_speed):
    if score < 20:
        meteor_speed = 5 * dificlty_multiplyer
    elif score < 40:
        meteor_speed = 8 * dificlty_multiplyer
    elif score < 60:
        meteor_speed = 12 * dificlty_multiplyer
    else:
        meteor_speed = 15 * dificlty_multiplyer
    return meteor_speed

#drop meteors
def meteor_fall(meteor_list):
    delay = random.random()
    if len(meteor_list) < 30 and delay < .25:
        x_pos = random.randint(0,WIDTH-meteor_Size)
        y_pos = 0
        meteor_list.append([x_pos, y_pos])

#draw meteors
def metero_draw(meteor_list):
    for meteor_pos in meteor_list:
        screen.blit(meteor, (meteor_pos[0], meteor_pos[1]))

#updates meteor/adds score
def meteor_up(meteor_list, score):
	for xyz, meteor_pos in enumerate(meteor_list):
        #moves meteor down
		if meteor_pos[1] >= 0 and meteor_pos[1] < HEIGHT:
			meteor_pos[1] += meteor_speed
        #adds score if meteor goes of screen
		else:
			meteor_list.pop(xyz)
			score += 1
	return score

#checks for player colision wih meteor
def collision_check(player_x, player_y, meteor_pos):
	for meteor_pos in meteor_list:
		if colision(player_x, player_y, meteor_pos):
			return True
	return False

#more colision
def colision(player_x, player_y, meteor_pos):
    p_x = player_x
    p_y = player_y

    m_x = meteor_pos[0]
    m_y = meteor_pos[1]
    if (m_x >= p_x and m_x < (p_x + player_Size)) or (p_x >= m_x and p_x < (m_x+meteor_Size)):
        if (m_y >= p_y and m_y < (p_y + player_Size)) or (p_y >= m_y and p_y < (m_y+meteor_Size)):
            return True
    return False

#message code
def display_message(message):
    pygame.time.delay(1000)
    win.fill((255,255,255))
    text = WORD_FONT.render(message, 1, (0,0,0))
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

#label code
def makeLabel(text, fontSize, xpos, ypos, fontColour='black', font='Arial', background="clear"):
    # make a text sprite
    thisText = newLabel(text, fontSize, font, fontColour, xpos, ypos, background)
    return thisText
def showLabel(labelName):
    textboxGroup.add(labelName)
    if screenRefresh:
        updateDisplay()

#textbox code
def makeTextBox(xpos, ypos, width, case=0, startingText="Please type here", maxLength=0, fontSize=22):
    thisTextBox = newTextBox(startingText, xpos, ypos, width, case, maxLength, fontSize)
    textboxGroup.add(thisTextBox)
    return thisTextBox
def showTextBox(textBoxName):
    textboxGroup.add(textBoxName)
    if screenRefresh:
        updateDisplay()
def textBoxInput(textbox, functionToCall=None, args=[]):
    # starts grabbing key inputs, putting into textbox until enter pressed
    global keydict
    textbox.text = ""
    returnVal = None
    while True:
        updateDisplay()
        if functionToCall:
            returnVal = functionToCall(*args)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    textbox.clear()
                    if returnVal:
                        return textbox.text, returnVal
                    else:
                        return textbox.text
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    textbox.update(event)
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

#scoreboard code
def fileWrite():
    #makes scren white
    screen.fill((255,255,255))

    #adds label
    nameinput = makeLabel("enter your name", 40, 30,30,"black")
    showLabel(nameinput)

    #text box
    wordbox = makeTextBox(60,30, 300, 0, "enter name here", 0, 24)
    showTextBox(wordBox)
    name = textBoxInput(wordbox)

    #stores data to file
    myFile = open("scoreboard.txt", "a")
    myFile.write(name + score)
    myFile.close()
    menu()

#character draw
def player_draw():
    KeyPress=pygame.key.get_pressed()
    global walkCount
    global player_x
    global speed
    global true
    global jump
    global jumpRight
    global jumpLeft
    global Left

    #sprite movement rendering code
    if walkCount + 1 >= SpriteFrames:
        walkCount = 0
    if left:
        Left = True
        if jump == True:
            screen.blit((jumpLeft), (player_x,player_y))
        else:
            screen.blit(walkLeft[walkCount//3],(player_x,player_y))
            walkCount += 1
    elif right:
        Left = False
        if jump == True:
            screen.blit((jumpRight), (player_x,player_y))
        else:
            screen.blit(walkRight[walkCount//3], (player_x,player_y))
            walkCount +=1
    else:
        if Left == True:
            screen.blit((characterLeft),(player_x,player_y))
            walkCount = 0
        else:
            screen.blit((characterRight),(player_x,player_y))
            walkCount = 0
    #screen update
    pygame.display.update()

#menu
def menu():
    global words
    global word
    global mx
    global my
    global run
    global click
    global dificlty_multiplyer

    loop = True
    while loop == True:
        #mouse position and white fill
        mx, my = pygame.mouse.get_pos()
        screen.fill((255,255,255))

        #buttons
        button_1 = pygame.Rect(105,295,200,50)
        button_2 = pygame.Rect(395,295,200,50)
        button_3 = pygame.Rect(695,295,200,50)
        button_4 = pygame.Rect(195,495,275,50)
        button_5 = pygame.Rect(565,495,200,50)
        pygame.draw.rect(screen, (255,0 ,0), button_1)
        pygame.draw.rect(screen, (255,0 ,0), button_2)
        pygame.draw.rect(screen, (255,0 ,0), button_3)
        pygame.draw.rect(screen, (255,0 ,0), button_4)
        pygame.draw.rect(screen, (255,0 ,0), button_5)

        #menu text
        text1 = TITLE_FONT.render("The Sky Is Falling", 1, (0,0,0))
        text2 = WORD_FONT.render("instructions", 1, (0,0,0))
        text2_0 = WORD_FONT.render("meteors will be falling from the sky", 1, (0,0,0))
        text2_1 = WORD_FONT.render("if you get hit you louse", 1, (0,0,0))
        text2_2 = WORD_FONT.render("use the left and right arow to move", 1, (0,0,0))
        text3 = WORD_FONT.render("easy", 1, (0,0,0))
        text4 = WORD_FONT.render("medium", 1, (0,0,0))
        text5 = WORD_FONT.render("hard", 1, (0,0,0))
        text6 = WORD_FONT.render("scoreboard", 1, (0,0,0))
        text7 = WORD_FONT.render("quit", 1, (0,0,0))
        #text display
        screen.blit(text1, (int(WIDTH/2 - (text1.get_width()/2)), 20))
        screen.blit(text2, (int(WIDTH/2 - text2.get_width()/2), 90))
        screen.blit(text2_0, (int(WIDTH/2 - text2_0.get_width()/2), 140))
        screen.blit(text2_1, (int(WIDTH/2 - text2_1.get_width()/2), 190))
        screen.blit(text2_2, (int(WIDTH/2 - text2_2.get_width()/2), 240))
        screen.blit (text3, (int(WIDTH/5 - text3.get_width()/2), 300))
        screen.blit(text4, (int(WIDTH/2 - text4.get_width()/2), 300))
        screen.blit(text5, (int(WIDTH/1.25 - text5.get_width()/2), 300))
        screen.blit(text6, (int(WIDTH/3 - text6.get_width()/2), 500))
        screen.blit(text7, (int(WIDTH/1.5 - text7.get_width()/2), 500))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
                break
        #if mouse left clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
        #button colision and action
        #easy
        if button_1.collidepoint((mx,my)):
            if click:
                screen.fill((0,0,0))
                score = 0
                dificlty = "easy"
                dificlty_multiplyer = 0.75
                pygame.display.update()
                loop = False
                main()
                pass
        #normal
        if button_2.collidepoint((mx,my)):
            if click:
                screen.fill((0,0,0))
                score = 0
                dificlty = "normal"
                dificlty_multiplyer = 1
                pygame.display.update()
                loop = False
                main()
                pass
        #Hard
        if button_3.collidepoint((mx,my)):
            if click:
                screen.fill((0,0,0))
                score = 0
                dificlty = "hard"
                dificlty_multiplyer = 2
                pygame.display.update()
                loop = False
                main()
                pass
        #scoreboard
        if button_4.collidepoint((mx,my)):
            if click:
                running = False
                pass
        #quit
        if button_5.collidepoint((mx,my)):
            if click:
                running = False
                break
        click = False

#main
def main():
    global running
    global player_x
    global player_y
    global jump
    global high
    global speed
    global Clock
    global right
    global left
    global alive
    global score
    global meteor_speed
    while running and alive:
        clock.tick(SpriteFrames)
        #exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
                break
        # movement
        KeyPress=pygame.key.get_pressed()
        #check what key was get_pressed
        if KeyPress[pygame.K_LEFT] and player_x > speed: #subtract from x left movement
            player_x -= speed
            left = True
            right = False
        elif KeyPress[pygame.K_RIGHT] and player_x < WIDTH - speed: #Add to x right movement
            player_x += speed
            left = False
            right = True
        #reset code when not moving
        else:
            left = False
            right = False
            walkCount = 0
        #jump code
        if not(jump): # moving y without jump
            if KeyPress[pygame.K_SPACE]:
                jump = True
                left = False
                right = False
                walkCount = 0
        else:
            if high >=-10:
                player_y -= (high*abs(high)) /2
                high -= 1
            else:
                high = 10
                jump = False
        screen.blit(background, (0,0))


        #meteor
        meteor_fall(meteor_list)
        score = meteor_up(meteor_list, score)
        meteor_speed = level_speed(score, meteor_speed)

        #score text
        DisplayScore = WORD_FONT.render("score: " + str(score), 1, (255,255,255))
        #display text
        screen.blit(DisplayScore, (WIDTH-200, HEIGHT-40))

        if collision_check(player_x, player_y, meteor_list) == True:
            alive = False
            dificlty = None
            dificlty_multiplyer = 1
            fileWrite()
            break

        metero_draw(meteor_list)
        player_draw()

        clock.tick(30)
        pygame.display.update()

menu()
pygame.quit()
