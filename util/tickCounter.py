def tick_update():
  global tick
  tick += 1

def tick_setup():
  global tick
  tick = 0

def isInterval(interval):
  global tick
  return tick % interval == 0