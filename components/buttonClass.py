# # Fake OOP because classes are not allowed in this project

# def constructor(**kwargs):
#     not_this = {}
#     for key, value in kwargs.items():
#         not_this[key] = value

# # saple method
# def sample_method(not_this):
#     for key, value in not_this.items():
#         print(key, value)
    

# Fake OOP because classes are not allowed in this project

from Processing3 import *
from util.triggerUtil import *

def button_constructor(x, y, width, height, text, textSize, textColor, buttonColor, hoverColor = None, textHoverColor = None, action = lambda: None):
    button = {}
    button["x"] = x
    button["y"] = y
    button["width"] = width
    button["height"] = height
    button["text"] = text
    button["textSize"] = textSize
    button["textColor"] = textColor
    button["buttonColor"] = buttonColor
    button["hoverColor"] = hoverColor
    button["action"] = action
    if textHoverColor == None:
        button["textHoverColor"] = textColor
    else:
        button["textHoverColor"] = textHoverColor

    if hoverColor == None:
        button["hoverColor"] = buttonColor
    else:
        button["hoverColor"] = hoverColor

    return button

def button_isHovered(button):
    half_width = button["width"] / 2
    half_height = button["height"] / 2
    return (button["x"] - half_width) <= mouseX <= (button["x"] + half_width) and (button["y"] - half_height) <= mouseY <= (button["y"] + half_height)

def button_draw(button):
    rectMode(CENTER)
    textAlign(CENTER, CENTER)
    if button["buttonColor"] != None:
        if button_isHovered(button):
            fill(button["hoverColor"])
        else:
            fill(button["buttonColor"])
        rect(button["x"], button["y"], button["width"], button["height"])
    
    if button_isHovered(button):
        fill(button["textHoverColor"])
    else:
        fill(button["textColor"])
    textSize(button["textSize"])
    text(button["text"], button["x"], button["y"])
    button_isClicked(button)

def button_isClicked(button):
    if button_isHovered(button) and mousePressedTrigger["state"]:
        button["action"]()
        return True
    return False


    

