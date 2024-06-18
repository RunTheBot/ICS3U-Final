# Compilation Strategy: dev.badbird.processing.compiler.strategy.impl.graph.GraphCompilationStrategy
# GRAPH:
# isDirected: true, allowsSelfLoops: false, nodes: [Scripts.CreateCircleMask.py, Scripts.CreateCircles.py, util.sunUtil.py, util.screenManager.py, classTemplate.py, util.transition.py, Screens.GameScreen.py, Screens.InstructionScreen.py, util.triggerUtil.py, components.fpsCounter.py, components.light.py, util.maskTransition.py, util.tickCounter.py, util.animation.py, Screens.MainMenu.py, main.py, components.button.py], edges: [<util.sunUtil.py -> util.animation.py>, <util.transition.py -> util.screenManager.py>, <util.transition.py -> util.animation.py>, <Screens.GameScreen.py -> components.light.py>, <Screens.GameScreen.py -> util.screenManager.py>, <Screens.InstructionScreen.py -> util.sunUtil.py>, <Screens.InstructionScreen.py -> util.screenManager.py>, <Screens.InstructionScreen.py -> components.button.py>, <util.maskTransition.py -> util.animation.py>, <util.maskTransition.py -> util.transition.py>, <Screens.MainMenu.py -> util.maskTransition.py>, <Screens.MainMenu.py -> util.screenManager.py>, <Screens.MainMenu.py -> components.button.py>, <Screens.MainMenu.py -> util.sunUtil.py>, <main.py -> util.maskTransition.py>, <main.py -> util.tickCounter.py>, <main.py -> Screens.MainMenu.py>, <main.py -> util.sunUtil.py>, <main.py -> util.screenManager.py>, <main.py -> components.button.py>, <main.py -> Screens.GameScreen.py>, <main.py -> Screens.InstructionScreen.py>, <main.py -> util.triggerUtil.py>, <main.py -> components.fpsCounter.py>, <components.button.py -> util.triggerUtil.py>]

# COMPILER_BEGIN: util.animation.py


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
        delay(1)
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
    
    

# COMPILER_END: util.animation.py

# COMPILER_BEGIN: util.screenManager.py
def switchScreen(screen, bypassCleanup=False):
    global currentScreen
    if not bypassCleanup:
        currentScreen["cleanup"]()
    currentScreen = screen
    currentScreen["init"]()
    print("Switched to screen: " + str(screen))

# COMPILER_END: util.screenManager.py

# COMPILER_BEGIN: util.transition.py


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
    
    
    
    

# COMPILER_END: util.transition.py

# COMPILER_BEGIN: util.maskTransition.py


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


    

# COMPILER_END: util.maskTransition.py

# COMPILER_BEGIN: util.tickCounter.py
def tick_update():
  global tick
  tick += 1

def tick_setup():
  global tick
  tick = 0

def isInterval(interval):
  global tick
  return tick % interval == 0

# COMPILER_END: util.tickCounter.py

# COMPILER_BEGIN: util.triggerUtil.py



def trigger_constructor( mode ):
    return {
        # "event": event,
        # "action": action,
        "mode": mode,
        "lastEventState": False,
        "state": False
    }

def trigger_update(trigger, event):
    global TriggerMode
    currentEventState = event
    state = False

    if trigger["mode"] == TriggerMode["RISING_EDGE"] and currentEventState and not trigger["lastEventState"]:
        state = True
        print("RISING EDGE")
    elif trigger["mode"] == TriggerMode["FALLING_EDGE"] and not currentEventState and trigger["lastEventState"]:
        state = True
        print("FALLING EDGE")
    elif trigger["mode"] == TriggerMode["REPEAT"] and currentEventState:
        state = True
        print("REPEAT")
    
    trigger["lastEventState"] = currentEventState
    trigger["state"] = state

def trigger_setup():
    global TriggerMode, mousePressedTrigger
    TriggerMode = {
        "RISING_EDGE": 1,
        "FALLING_EDGE": 2,
        "REPEAT": 3
    }
    mousePressedTrigger = trigger_constructor(TriggerMode["RISING_EDGE"])
    mouseReleasedTrigger = trigger_constructor(TriggerMode["FALLING_EDGE"])


# COMPILER_END: util.triggerUtil.py

# COMPILER_BEGIN: components.button.py
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


    


# COMPILER_END: components.button.py

# COMPILER_BEGIN: util.sunUtil.py


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


# COMPILER_END: util.sunUtil.py

# COMPILER_BEGIN: Screens.MainMenu.py
import uuid


def mainMenu_draw():
    draw_sun()


def mainMenu_init():
    global buttons, centerX, SCREENS, commands, mainMusic
    buttons = []
    sizeX, sizeY = 100, 50  # Button size
    buttonCenterX = centerX - sizeX / 2
    textSize = 20
    textColor = color(255)
    buttonHover = None
    textHover = color(200, 200, 200)
    fill(255)
    
    mainMusic.play()

    loadSun()

    buttons.append(
        button_constructor(
            centerX, 
            500, 
            sizeX, 
            sizeY, 
            "Play", 
            textSize, 
            textColor, 
            None, 
            buttonHover,
            textHover,
            lambda: commands.setdefault(str(uuid.uuid4()), maskTransition_draw)
        )
    )
    buttons.append(
        button_constructor(
            centerX, 
            600, 
            sizeX, 
            sizeY, 
            "Instructions", 
            textSize, 
            textColor, 
            None, 
            buttonHover,
            textHover,
            lambda: switchScreen(SCREENS["INSTRUCTIONS"], True)
            
        )
    )
def mainMenu_cleanup():
    sun_cleanup()

# COMPILER_END: Screens.MainMenu.py

# COMPILER_BEGIN: components.light.py

import uuid
def light_setup():
    global lightAssets, lights, currDraggingLight
    lights = {}
    lightAssets = {}
    currDraggingLight = None

def light_load(i):
    global lightAssets, lights
    if i in lightAssets:
        return lightAssets[i]
    else:
        lightAssets[i] = loadImage("light/light_" + str(i) + ".png")
        return lightAssets[i]

def light_constructor(size, x, y):
    global lights
    light_uuid = str(uuid.uuid4())
    lights[light_uuid] = {
        "size": size,
        "radius": ((size + 0.5) * 8) - 4,
        "x": x,
        "y": y,
        "uuid": light_uuid,
    }
    return light_uuid

def light_draw(light):
    global centerX, centerY

    imageMode(CENTER)
    image(light_load(light["size"]), light["x"], light["y"])
    if False:
        # draw a circle as radius
        stroke(255, 0, 0)
        strokeWeight(2)
        fill(0, 0, 0, 0)
        ellipse(light["x"], light["y"], light["radius"] * 2, light["radius"] * 2)

def light_merge(light1, light2):
    global lights, centerLight
    # make sure light1 is the bigger one
    if light1["size"] < light2["size"]:
        light1, light2 = light2, light1
    
    # Make sure light2 is not the center light
    if light2["uuid"] == centerLight:
        light1, light2 = light2, light1

    light1OriginalSize = light1["size"]

    # add the size of the smaller light to the bigger one
    lights[light1["uuid"]]["size"] += lights[light2["uuid"]]["size"]
    # Recalculate the radius
    lights[light1["uuid"]]["radius"] = ((lights[light1["uuid"]]["size"] + 0.5) * 8) - 4

    if light1OriginalSize > 7:
        if lightAssets.get(light1OriginalSize) != None:
            del lightAssets[light1OriginalSize]

    global vineBoomSound
    vineBoomSound.rewind()
    vineBoomSound.play()

    print("Merged", light1["uuid"], light2["uuid"])
    # remove the smaller light
    del lights[light2["uuid"]]

def light_checkCollision():
    global lights
    for light_key in lights.keys():
        for otherLight_key in lights.keys():
            light = lights.get(light_key)
            otherLight = lights.get(otherLight_key)
            if light == None or otherLight == None:
                continue
            if light["uuid"] == otherLight["uuid"]:
                continue
            
            # if they touch merge them
            center_distance = sqrt((light["x"] - otherLight["x"])**2 + (light["y"] - otherLight["y"])**2)
            if center_distance < light["radius"] + otherLight["radius"]:
                light_merge(light, otherLight)

def light_drawAll():
    global lights
    for light in lights.values():
        print(light["x"], light["y"])
        light_draw(light)
    handleDrag()
    light_checkCollision()


def light_getHovered():
    for light in lights.values():
        if light["x"] + light["radius"] > mouseX and light["x"] - light["radius"] < mouseX:
            if light["y"] + light["radius"] > mouseY and light["y"] - light["radius"] < mouseY:
                return light
    return None

def handleDrag():
    global currDraggingLight

    # if currDraggingLight == None and mousePressed and mouseButton == LEFT:
    #     currDraggingLight = light_getHovered()
    # else:
    #     currDraggingLight = None

    if mousePressed and mouseButton == LEFT:
        if currDraggingLight == None:
            currDraggingLight = light_getHovered()
    else:
        currDraggingLight = None

    if currDraggingLight != None:
        # draw a dot as a visual cue
        # stroke(255, 0, 0)
        # strokeWeight(2)
        # fill(0, 0, 0, 0)
        # ellipse(currDraggingLight["x"], currDraggingLight["y"], 10, 10)
        currDraggingLight["x"] = mouseX
        currDraggingLight["y"] = mouseY

# COMPILER_END: components.light.py

# COMPILER_BEGIN: Screens.GameScreen.py
import random

import time

def gameScreen_draw():
    global nextSpawnTicks, centerLight, centerX, centerY, lights, bird, timer, minim, winMusic, looseMusic, mainMusic
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
        mainMusic.rewind()
        mainMusic.pause()
        winMusic.play()
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

    fill(0)
    noStroke()
    rect(width - 100, 50, 200, 20)

    fill(255)

    minutes = int(remaining_time // 60)
    seconds = int(remaining_time % 60)
    time_text = "Time: {:02d}:{:02d}".format(minutes, seconds)
    text(time_text, width - 100, 50)


    if remaining_time <= 0:
        nextSpawnTicks = 100000
        background(0)
        fill(255)
        text("Game Over! The darkness consumed you.", centerX, centerY, 20)
        text("Press any key to continue", centerX, centerY + 50, 20)
        mainMusic.rewind()
        mainMusic.pause()
        looseMusic.play()
        if keyPressed:
            lights = {}
            switchScreen(SCREENS["MAIN_MENU"])
        fill(0)



def gameScreen_init():
    global buttons, centerX, centerY, SCREENS, nextSpawnTicks, lights, centerLight, bird, start_time, end_time, mainMusic, winMusic, looseMusic

    start_time = time.time()
    end_time = start_time + 60

    nextSpawnTicks = random.randint(180, 660)
    bird = loadImage("bird.png")
    buttons = []
    centerLight = light_constructor(7, random.randint(0, width), random.randint(0, height))

    winMusic.rewind()
    looseMusic.rewind()

def gameScreen_cleanup():
    global bird, lights, centerLight, winMusic, looseMusic
    winMusic.rewind()
    looseMusic.rewind()
    winMusic.pause()
    looseMusic.pause()
    



# COMPILER_END: Screens.GameScreen.py

# COMPILER_BEGIN: Screens.InstructionScreen.py



def instructions_draw():
    global buttons, sun, tick, centerX, centerY
    draw_sun()
    textSize(32)
    fill(255)
    text("Instructions", centerX, 100)
    textSize(20)
    fill(255)
    text("Use the 'esc' key to return to the main menu", centerX, 400)
    text("Make sure to be fast and fight the drakness", centerX, 450)
    text("Use Mouse to move bird around", centerX, 500)
    text("Click and drage the light together to merge them", centerX, 550)

def instructions_init():
    # # back button
    global buttons, centerX, SCREENS
    buttons = []
    sizeX, sizeY = 50, 50  # Button size
    textSize = 20
    textColor = color(255)
    buttonHover = None
    textHover = color(200, 200, 200)

    buttons.append(
        button_constructor(
            centerX, 
            600, 
            sizeX, 
            sizeY, 
            "Back", 
            textSize, 
            textColor, 
            None, 
            buttonHover,
            textHover,
            lambda: switchScreen(SCREENS["MAIN_MENU"])
        )
    )

# COMPILER_END: Screens.InstructionScreen.py

# COMPILER_BEGIN: components.fpsCounter.py


def fpsCounter_draw():
    fill(255)
    textSize(12)
    text("FPS: " + str(int(frameRate)), 10, 20)

# COMPILER_END: components.fpsCounter.py

# COMPILER_BEGIN: main.py


add_library('minim') #!Compliler_

def setup():
    size(1280, 720)
    global tick, buttons, sun, centerX, centerY, SCREENS, currentScreen, commands, minim, vineBoomSound, sun, sky, mainMusic, winMusic, looseMusic
    sun = None
    sky = None
    centerX, centerY = width // 2, height // 2
    buttons = []
    commands = {}
    tick_setup()
    trigger_setup()
    light_setup()
    minim=Minim(this)

    mainMusic = minim.loadFile("game.mp3")
    vineBoomSound = minim.loadFile("vineboom.mp3")
    winMusic = minim.loadFile("win.mp3")
    looseMusic = minim.loadFile("loose.mp3")
    mainMusic.play()
    mainMusic.loop()
    
    # Screen manager setup
    global currentScreen, SCREENS

    SCREENS = {
        "MAIN_MENU": {
            "draw": mainMenu_draw,
            "setup": lambda: None,
            "init": mainMenu_init,
            "cleanup": mainMenu_cleanup
        },
        "GAME": {
            "draw": gameScreen_draw,
            "setup": lambda: None,
            "init": gameScreen_init,
            "cleanup": gameScreen_cleanup
        },
        "INSTRUCTIONS": {
            "draw": instructions_draw,
            "setup": lambda: None,
            "init": instructions_init,
            "cleanup": lambda: None
        }
    }

    maskTransition_setup()

    font = createFont("Minecraft.ttf", 50)
    textFont(font)

    currentScreen = SCREENS["MAIN_MENU"]
    currentScreen["init"]()


def draw():
    global buttons, mousePressedTrigger

    tick_update()
    noStroke()
    background(0)
    fpsCounter_draw()

    trigger_update(mousePressedTrigger, mousePressed)

    currentScreen["draw"]()
    for button in buttons:
        button_draw(button)

    for uuid, command in commands.items():
        if command():
            del commands[uuid]
        


    
        

# COMPILER_END: main.py

