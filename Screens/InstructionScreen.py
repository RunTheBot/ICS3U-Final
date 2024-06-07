from Processing3 import *
from components.button import *
from util.sunUtil import draw_sun
from util.screenManager import *


def instructions_draw():
    global buttons, sun, tick, centerX, centerY
    draw_sun()
    textSize(32)
    fill(255)
    text("Instructions (All is Placeholder)", centerX, 100)
    textSize(20)
    fill(255)
    text("Use the 'esc' key to return to the main menu", centerX, 400)
    text("Use the 'q' key to quit the game", centerX, 450)
    text("Defeat the enemies to win", centerX, 500)
    text("Good luck!", centerX, 550)

def instructions_init():
    # # back button
    global buttons, centerX, SCREENS
    buttons = []
    sizeX, sizeY = 50, 50  # Button size
    textSize = 20
    textColor = color(255)
    buttonHover = None
    textHover = color(200, 200, 200)

    buttons.append(
        button_constructor(
            centerX, 
            600, 
            sizeX, 
            sizeY, 
            "Back", 
            textSize, 
            textColor, 
            None, 
            buttonHover,
            textHover,
            lambda: switchScreen(SCREENS["MAIN_MENU"])
        )
    )