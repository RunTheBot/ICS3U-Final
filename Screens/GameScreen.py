import random

from components.light import *

def gameScreen_draw():
    global nextSpawnTicks
    if nextSpawnTicks <= 0: 
        print("Spawning")
        nextSpawnTicks = random.randint(120, 600)
        light_constructor(7, random.randint(0, width), random.randint(0, height))
    light_drawAll()

    
    nextSpawnTicks -= 1

def gameScreen_init():
    global buttons, centerX, centerY, SCREENS, nextSpawnTicks, lights
    nextSpawnTicks = 0
    buttons = []
    light_constructor(7, centerX, centerY)
