from Processing3 import *
from util.animation import *

def sun_numberProcessor(i):
    return str(i).zfill(3)
def sky_numberProcessor(i):
    return str(i).zfill(2)

def loadSun():
    global sun, sky
    # sun = []
    # for i in range(300):
    #     # there are images labeled from 000 to 299
    #     sun.append(loadImage("sun/sunYellow" + str(i).zfill(3) + ".gif"))
    if sun == None or len(sun) == 0:
        sun = load_animation("sun/sunYellow", ".gif", 0, 300, 2, (centerX, centerY-110), sun_numberProcessor)
    if sky == None or len(sky) == 0:
        sky = load_animation("sun/sky/sky", ".gif", 0, 42, 10, (centerX, centerY), sky_numberProcessor)

def draw_sun():
    global sun, sky, tick, centerX, centerY
    # sunFrame = int(tick / 2) % 300
    # imageMode(CENTER)
    # image(sun[sunFrame], centerX, centerY-110)
    play_animation(sky)
    draw_animation(sky)
    play_animation(sun)
    draw_animation(sun)

def sun_cleanup():
    global sun, sky
    del sun
    del sky
    sun = None
    sky = None

