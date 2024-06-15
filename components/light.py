from Processing3 import *
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
    if True:
        # draw a circle as radius
        stroke(255, 0, 0)
        strokeWeight(2)
        fill(0, 0, 0, 0)
        ellipse(light["x"], light["y"], light["radius"] * 2, light["radius"] * 2)

def light_merge(light1, light2):
    global lights
    # make sure light1 is the bigger one
    if light1["size"] < light2["size"]:
        light1, light2 = light2, light1
    # add the size of the smaller light to the bigger one
    lights[light1["uuid"]]["size"] += lights[light2["uuid"]]["size"]
    # Recalculate the radius
    lights[light1["uuid"]]["radius"] = ((lights[light1["uuid"]]["size"] + 0.5) * 8) - 4

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
        stroke(255, 0, 0)
        strokeWeight(2)
        fill(0, 0, 0, 0)
        ellipse(currDraggingLight["x"], currDraggingLight["y"], 10, 10)
        currDraggingLight["x"] = mouseX
        currDraggingLight["y"] = mouseY
