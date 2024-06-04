from Processing3 import *
from util.tickCounter import *
from components.buttonClass import *
from components.fpsCounter import *
from Screens.MainMenu import *
from util.screenManager import *
from util.loadSun import *
from Screens.InstructionScreen import *
from util.triggerUtil import *


def setup():
    size(1280, 720)
    global tick, buttons, sun, centerX, centerY, SCREENS, currentScreen
    centerX, centerY = width // 2, height // 2
    buttons = []
    loadSun()
    tick_setup()
    trigger_setup()
    # Screen manager setup
    global currentScreen, SCREENS

    SCREENS = {
        "MAIN_MENU": {
            "draw": mainMenu_draw,
            "setup": lambda: None,
            "init": mainMenu_init
        },
        "GAME": 1,
        "INSTRUCTIONS": {
            "draw": instructions_draw,
            "setup": lambda: None,
            "init": instructions_init
        
        },
        "CREDITS": 3,
        "GAME_OVER": 4
    }

    currentScreen = SCREENS["MAIN_MENU"]
    currentScreen["init"]()

def draw():
    global buttons, mousePressedTrigger

    tick_update()
    noStroke()
    background(0)
    fpsCounter_draw()

    trigger_update(mousePressedTrigger, mousePressed)

    currentScreen["draw"]()
    for button in buttons:
        button_draw(button)

    
        