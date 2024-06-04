# Compilation Strategy: dev.badbird.processing.compiler.strategy.impl.graph.GraphCompilationStrategy
# GRAPH:
# isDirected: true, allowsSelfLoops: false, nodes: [util.loadSun.py, util.tickCounter.py, Screens.MainMenu.py, main.py, util.screenManager.py, classTemplate.py, components.buttonClass.py, characterClass.py, Screens.InstructionScreen.py, util.triggerUtil.py, components.fpsCounter.py], edges: [<Screens.MainMenu.py -> util.screenManager.py>, <Screens.MainMenu.py -> components.buttonClass.py>, <main.py -> util.tickCounter.py>, <main.py -> util.loadSun.py>, <main.py -> util.screenManager.py>, <main.py -> components.buttonClass.py>, <main.py -> Screens.MainMenu.py>, <main.py -> Screens.InstructionScreen.py>, <main.py -> util.triggerUtil.py>, <main.py -> components.fpsCounter.py>, <components.buttonClass.py -> util.triggerUtil.py>, <Screens.InstructionScreen.py -> util.screenManager.py>, <Screens.InstructionScreen.py -> components.buttonClass.py>]

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

# COMPILER_BEGIN: util.loadSun.py
def loadSun():
    global sun
    sun = []
    for i in range(300):
        # there are images labeled from 000 to 299
        sun.append(loadImage("sunYellow" + str(i).zfill(3) + ".gif"))

# COMPILER_END: util.loadSun.py

# COMPILER_BEGIN: util.screenManager.py
def switchScreen(screen):
    global currentScreen
    currentScreen = screen
    currentScreen["init"]()
    print("Switched to screen: " + str(screen))

# COMPILER_END: util.screenManager.py

# COMPILER_BEGIN: util.triggerUtil.py



# Define the Trigger constructor
def trigger_constructor( mode ):
    return {
        # "event": event,
        # "action": action,
        "mode": mode,
        "lastEventState": False,
        "state": False
    }

# Define the Trigger update method
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
    # Define the TriggerMode enum
    # Define the TriggerMode dict
    TriggerMode = {
        "RISING_EDGE": 1,
        "FALLING_EDGE": 2,
        "REPEAT": 3
    }
    # MousePressed as an example
    mousePressedTrigger = trigger_constructor(TriggerMode["RISING_EDGE"])


# COMPILER_END: util.triggerUtil.py

# COMPILER_BEGIN: components.buttonClass.py
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


    


# COMPILER_END: components.buttonClass.py

# COMPILER_BEGIN: Screens.MainMenu.py


def mainMenu_draw():
    global buttons, sun, tick, centerX, centerY
    sunFrame = int(tick / 2) % 300
    imageMode(CENTER)
    image(sun[sunFrame], centerX, centerY-110, 512, 512)


def mainMenu_init():
    global buttons, centerX, SCREENS
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
            lambda: switchScreen(SCREENS["GAME"])
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
    sunFrame = int(tick / 2) % 300
    imageMode(CENTER)
    image(sun[sunFrame], centerX, centerY-110, 512, 512)
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
    global tick, buttons, sun, centerX, centerY, SCREENS, currentScreen
    centerX, centerY = width // 2, height // 2
    buttons = []
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

    
        

# COMPILER_END: main.py

