from Processing3 import *
from util.screenManager import *
from util.animation import *

def transition_construtor(animation, nextScreen):
    return {
        "animation": animation,
        "nextScreen": nextScreen
    }

def transition_play(transition):
    global currentScreen
    print("Transitioning to screen: " + str(transition["nextScreen"]))
    play_animation(transition["animation"])
    if transition["animation"]["looped"]:
        background(0)
        switchScreen(transition["nextScreen"])
        return True
    draw_animation(transition["animation"])
    return False
    
    
    
    