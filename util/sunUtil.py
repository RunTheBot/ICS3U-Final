from Processing3 import *
from util.animation import *

def sun_numberProcessor(i):
    return str(i).zfill(3)

def loadSun():
    global sun
    # sun = []
    # for i in range(300):
    #     # there are images labeled from 000 to 299
    #     sun.append(loadImage("sun/sunYellow" + str(i).zfill(3) + ".gif"))
    sun = load_animation("sun/sunYellow", ".gif", 0, 300, 2, (centerX, centerY-110), sun_numberProcessor)

def draw_sun():
    global sun, tick, centerX, centerY
    # sunFrame = int(tick / 2) % 300
    # imageMode(CENTER)
    # image(sun[sunFrame], centerX, centerY-110)
    play_animation(sun)
    draw_animation(sun)