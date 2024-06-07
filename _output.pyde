# Compilation Strategy: dev.badbird.processing.compiler.strategy.impl.graph.GraphCompilationStrategy
# GRAPH:
# isDirected: true, allowsSelfLoops: false, nodes: [Scripts.CreateCircleMask.py, util.sunUtil.py, util.screenManager.py, classTemplate.py, util.transition.py, characterClass.py, Screens.InstructionScreen.py, util.triggerUtil.py, components.fpsCounter.py, util.maskTransition.py, util.tickCounter.py, util.animation.py, Screens.MainMenu.py, main.py, components.button.py], edges: [<util.sunUtil.py -> util.animation.py>, <util.transition.py -> util.screenManager.py>, <util.transition.py -> util.animation.py>, <Screens.InstructionScreen.py -> util.sunUtil.py>, <Screens.InstructionScreen.py -> util.screenManager.py>, <Screens.InstructionScreen.py -> components.button.py>, <util.maskTransition.py -> util.animation.py>, <util.maskTransition.py -> util.transition.py>, <Screens.MainMenu.py -> util.maskTransition.py>, <Screens.MainMenu.py -> util.screenManager.py>, <Screens.MainMenu.py -> components.button.py>, <Screens.MainMenu.py -> util.sunUtil.py>, <main.py -> util.maskTransition.py>, <main.py -> util.tickCounter.py>, <main.py -> Screens.MainMenu.py>, <main.py -> util.sunUtil.py>, <main.py -> util.screenManager.py>, <main.py -> components.button.py>, <main.py -> Screens.InstructionScreen.py>, <main.py -> util.triggerUtil.py>, <main.py -> components.fpsCounter.py>, <components.button.py -> util.triggerUtil.py>]

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
def switchScreen(screen):
    global currentScreen
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

# COMPILER_END: util.sunUtil.py

# COMPILER_BEGIN: Screens.MainMenu.py


def mainMenu_draw():
    draw_sun()


def mainMenu_init():
    global buttons, centerX, SCREENS, commands
    buttons = []
    sizeX, sizeY = 100, 50  # Button size
    buttonCenterX = centerX - sizeX / 2
    textSize = 20
    textColor = color(255)
    buttonHover = None
    textHover = color(200, 200, 200)

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
            lambda: commands.append(maskTransition_draw)
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
            lambda: switchScreen(SCREENS["INSTRUCTIONS"])
            
        )
    )

# COMPILER_END: Screens.MainMenu.py

# COMPILER_BEGIN: Screens.InstructionScreen.py



def instructions_draw():
    global buttons, sun, tick, centerX, centerY
    draw_sun()
    textSize(32)
    fill(255)
    text("Instructions (All is Placeholder)", centerX, 100)
    textSize(20)
    fill(255)
    text("Use the 'esc' key to return to the main menu", centerX, 400)
    text("Use the 'q' key to quit the game", centerX, 450)
    text("Defeat the enemies to win", centerX, 500)
    text("Good luck!", centerX, 550)

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



def setup():
    size(1280, 720)
    global tick, buttons, sun, centerX, centerY, SCREENS, currentScreen, commands
    centerX, centerY = width // 2, height // 2
    buttons = []
    commands = []
    loadSun()
    tick_setup()
    trigger_setup()
    # Screen manager setup
    global currentScreen, SCREENS

    SCREENS = {
        "MAIN_MENU": {
            "draw": mainMenu_draw,
            "setup": lambda: None,
            "init": mainMenu_init
        },
        "GAME": 1,
        "INSTRUCTIONS": {
            "draw": instructions_draw,
            "setup": lambda: None,
            "init": instructions_init
        
        },
        "CREDITS": 3,
        "GAME_OVER": 4
    }

    maskTransition_setup()

    currentScreen = SCREENS["MAIN_MENU"]
    currentScreen["init"]()

def draw():
    global buttons, mousePressedTrigger

    tick_update()
    noStroke()
    background(128)
    fpsCounter_draw()

    trigger_update(mousePressedTrigger, mousePressed)

    currentScreen["draw"]()
    for button in buttons:
        button_draw(button)
    
    for idx, command in enumerate(commands):
        if command():
            commands.pop(idx)
        


    
        

# COMPILER_END: main.py

