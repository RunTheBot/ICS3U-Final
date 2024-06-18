def switchScreen(screen, bypassCleanup=False):
    global currentScreen
    if not bypassCleanup:
        currentScreen["cleanup"]()
    currentScreen = screen
    currentScreen["init"]()
    print("Switched to screen: " + str(screen))