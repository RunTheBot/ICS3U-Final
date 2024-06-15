import random

from components.light import *
from util.screenManager import *

def gameScreen_draw():
    global nextSpawnTicks, centerLight, centerX, centerY, lights, bird
    lights[centerLight]["x"] = centerX
    lights[centerLight]["y"] = centerY
    if nextSpawnTicks <= 0: 
        print("Spawning")
        nextSpawnTicks = random.randint(180, 660)
        light_constructor(random.randint(0, 4), random.randint(0, width), random.randint(0, height))
    light_drawAll()

    image(bird, mouseX, mouseY, 100, 100)

    if lights[centerLight]["size"] > 91:
        nextSpawnTicks = 100000
        textSize = 20
        fill(0)
        text("Game You Win!", centerX, centerY, textSize)
        text("Press any key to continue", centerX, centerY + 50, textSize)
        if keyPressed:
            lights = {}
            switchScreen(SCREENS["MAIN_MENU"])
        fill(255)
    
    nextSpawnTicks -= 1

def gameScreen_init():
    global buttons, centerX, centerY, SCREENS, nextSpawnTicks, lights, centerLight, bird
    nextSpawnTicks = random.randint(180, 660)
    bird = loadImage("bird.png")
    buttons = []
    centerLight = light_constructor(92, random.randint(0, width), random.randint(0, height))
