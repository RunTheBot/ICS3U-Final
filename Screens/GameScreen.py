import random

from components.light import *
from util.screenManager import *
import time

def gameScreen_draw():
    global nextSpawnTicks, centerLight, centerX, centerY, lights, bird, timer
    lights[centerLight]["x"] = centerX
    lights[centerLight]["y"] = centerY
    if nextSpawnTicks <= 0: 
        print("Spawning")
        nextSpawnTicks = random.randint(100-lights[centerLight]["size"], 300-lights[centerLight]["size"]*2)
        light_constructor(random.randint(0, 7), random.randint(0, width), random.randint(0, height))
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
        return
    
    nextSpawnTicks -= 1


    current_time = time.time()
    elapsed_time = current_time - start_time
    remaining_time = end_time - current_time

    fill(255)

    minutes = int(remaining_time // 60)
    seconds = int(remaining_time % 60)
    time_text = "Time: {:02d}:{:02d}".format(minutes, seconds)
    text(time_text, width - 100, 50)

    if remaining_time <= 0:
        background(0)
        fill(255)
        text("Game Over! The darkness consumed you.", centerX, centerY, 20)
        text("Press any key to continue", centerX, centerY + 50, 20)
        if keyPressed:
            lights = {}
            switchScreen(SCREENS["MAIN_MENU"])
        fill(0)


def gameScreen_init():
    global buttons, centerX, centerY, SCREENS, nextSpawnTicks, lights, centerLight, bird, start_time, end_time

    start_time = time.time()
    end_time = start_time + 240

    nextSpawnTicks = random.randint(180, 660)
    bird = loadImage("bird.png")
    buttons = []
    centerLight = light_constructor(7, random.randint(0, width), random.randint(0, height))
