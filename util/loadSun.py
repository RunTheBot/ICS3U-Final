from Processing3 import *

def loadSun():
    global sun
    sun = []
    for i in range(300):
        # there are images labeled from 000 to 299
        sun.append(loadImage("sun/sunYellow" + str(i).zfill(3) + ".gif"))

def draw_sun():
    global sun, tick, centerX, centerY
    sunFrame = int(tick / 2) % 300
    imageMode(CENTER)
    image(sun[sunFrame], centerX, centerY-110)