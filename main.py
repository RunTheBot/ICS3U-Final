from Processing3 import *
from Screens.GameScreen import *
from util.maskTransition import *
from util.tickCounter import *
from components.button import *
from components.fpsCounter import *
from Screens.MainMenu import *
from util.screenManager import *
from util.sunUtil import *
from Screens.InstructionScreen import *
from util.triggerUtil import *

add_library('minim') #!Compliler_

def setup():
    size(1280, 720)
    global tick, buttons, sun, centerX, centerY, SCREENS, currentScreen, commands, minim, vineBoomSound, sun, sky, mainMusic, winMusic, looseMusic
    sun = None
    sky = None
    centerX, centerY = width // 2, height // 2
    buttons = []
    commands = {}
    tick_setup()
    trigger_setup()
    light_setup()
    minim=Minim(this)

    mainMusic = minim.loadFile("game.mp3")
    vineBoomSound = minim.loadFile("vineboom.mp3")
    winMusic = minim.loadFile("win.mp3")
    looseMusic = minim.loadFile("loose.mp3")
    mainMusic.play()
    mainMusic.loop()
    
    # Screen manager setup
    global currentScreen, SCREENS

    SCREENS = {
        "MAIN_MENU": {
            "draw": mainMenu_draw,
            "setup": lambda: None,
            "init": mainMenu_init,
            "cleanup": mainMenu_cleanup
        },
        "GAME": {
            "draw": gameScreen_draw,
            "setup": lambda: None,
            "init": gameScreen_init,
            "cleanup": gameScreen_cleanup
        },
        "INSTRUCTIONS": {
            "draw": instructions_draw,
            "setup": lambda: None,
            "init": instructions_init,
            "cleanup": lambda: None
        }
    }

    maskTransition_setup()

    font = createFont("Minecraft.ttf", 50)
    textFont(font)

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

    for uuid, command in commands.items():
        if command():
            del commands[uuid]
        


    
        