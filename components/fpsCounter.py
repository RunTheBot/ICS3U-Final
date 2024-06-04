from Processing3 import *

def fpsCounter_draw():
    fill(255)
    textSize(12)
    text("FPS: " + str(int(frameRate)), 10, 20)