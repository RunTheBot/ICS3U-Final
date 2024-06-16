def switchScreen(screen):
    global currentScreen
    currentScreen["cleanup"]()
    currentScreen = screen
    currentScreen["init"]()
    print("Switched to screen: " + str(screen))