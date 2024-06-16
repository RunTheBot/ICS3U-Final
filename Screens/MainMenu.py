import uuid
from Processing3 import *
from components.button import *
from util.sunUtil import *
from util.screenManager import *
from util.maskTransition import *

def mainMenu_draw():
    draw_sun()


def mainMenu_init():
    global buttons, centerX, SCREENS, commands
    buttons = []
    sizeX, sizeY = 100, 50  # Button size
    buttonCenterX = centerX - sizeX / 2
    textSize = 20
    textColor = color(255)
    buttonHover = None
    textHover = color(200, 200, 200)
    fill(255)
    text("Loading...", centerX, 50)

    loadSun()

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
            lambda: commands.setdefault(str(uuid.uuid4()), maskTransition_draw)
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
def mainMenu_cleanup():
    sun_cleanup()