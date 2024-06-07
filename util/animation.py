from Processing3 import *

def load_animation(base_path_prefix, base_path_sufix, start, end, frame_rate=10, pos=(0, 0), numberProcessor=lambda x: x, reversed=False):
    animation = {
        "frame": 0,
        "speed": frame_rate,
        "tickSinceLastFrame": 0,
        "animation": [],
        "looped": False,
        "pos": pos
    }
    step = -1 if reversed else 1
    if reversed:
        end, start = start-1, end-1

    for i in range(start, end, step):
        animation["animation"].append(loadImage(base_path_prefix + str(numberProcessor(i)) + base_path_sufix))
    return animation

def draw_animation(animation):
    global tick
    imageMode(CENTER)
    image(animation["animation"][animation["frame"]], animation["pos"][0], animation["pos"][1])

def play_animation(animation):
    # tick increments 60 times per second
    animation["tickSinceLastFrame"] += 1
    if animation["tickSinceLastFrame"] >= animation["speed"]:
        animation["tickSinceLastFrame"] = 0
        animation["frame"] += 1
        if animation["frame"] >= len(animation["animation"]):
            animation["frame"] = 0
            if not animation["looped"]:
                animation["looped"] = True
    
    
