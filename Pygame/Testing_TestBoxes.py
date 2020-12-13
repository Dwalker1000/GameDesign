import pygame, os

pygame.init()
WIDTH = 1000 # screen width
HEIGHT = 800 # screen height
screen = pygame.display.set_mode((WIDTH,HEIGHT))
x = True
#scoreboard code

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
while x == True:
    fileWrite()
