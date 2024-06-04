from Processing3 import *


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

