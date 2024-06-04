def loadSun():
    global sun
    sun = []
    for i in range(300):
        # there are images labeled from 000 to 299
        sun.append(loadImage("sunYellow" + str(i).zfill(3) + ".gif"))