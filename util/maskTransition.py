from Processing3 import *
from util.animation import *
from util.transition import *

def maskTransition_setup():
    global maskTransition, centerX, centerY, SCREENS

    # Loop through the numbers from 0 to 91
    # for i in range(92):
    #     # Construct the file path
    #     file_path = "animation/circle_mask_" + str(i) + ".png"

    #     # Load the image
    #     img = loadImage(file_path)

    #     # Append the image to the list
    #     maskTransition_images.append(img)

    maskTransition = transition_construtor(load_animation("animation/circle_mask_", ".png", 0, 92, 1, (centerX, centerY), reversed=True), SCREENS["GAME"])

def maskTransition_draw():
    global maskTransition

    # Draw the current frame
    return transition_play(maskTransition)


    