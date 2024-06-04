from Processing3 import *
from components.buttonClass import *
from util.screenManager import *

def mainMenu_draw():
    global buttons, sun, tick, centerX, centerY
    sunFrame = int(tick / 2) % 300
    imageMode(CENTER)
    image(sun[sunFrame], centerX, centerY-110, 512, 512)


def mainMenu_init():
    global buttons, centerX, SCREENS
    buttons = []
    sizeX, sizeY = 100, 50  # Button size
    buttonCenterX = centerX - sizeX / 2
    textSize = 20
    textColor = color(255)
    buttonHover = None
    textHover = color(200, 200, 200)

    buttons.append(
        button_constructor(
            centerX, 
            500, 
            sizeX, 
            sizeY, 
            "Play", 
            textSize, 
            textColor, 
            None, 
            buttonHover,
            textHover,
            lambda: switchScreen(SCREENS["GAME"])
        )
    )
    buttons.append(
        button_constructor(
            centerX, 
            600, 
            sizeX, 
            sizeY, 
            "Instructions", 
            textSize, 
            textColor, 
            None, 
            buttonHover,
            textHover,
            lambda: switchScreen(SCREENS["INSTRUCTIONS"])
            
        )
    )