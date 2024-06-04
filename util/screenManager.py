def switchScreen(screen):
    global currentScreen
    currentScreen = screen
    currentScreen["init"]()
    print("Switched to screen: " + str(screen))