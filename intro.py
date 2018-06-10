# a window 20 grid blocks wide by 15 grid height
WIDTH = 25
HEIGHT = 15

# title of the window
TITLE = 'Piggy Revenge'

# use a background image
background('bg2')

# ground tiles
image('ground1', pos=(0,14), tag=OBSTACLE)
for x in range(1, WIDTH-1, 1):
   image('ground2', pos=(x, 14), tag=OBSTACLE)
image('ground3', pos=(WIDTH-1,14), tag=OBSTACLE)

# create Porter, give him a mass so he falls down, use arrow keys to move left/right
p = actor('Porter', pos=(0,12), size=2, tag='Porter').speed(3)

# throw a punch on the return/enter key
keydown('return', partial(p.act, ATTACK, 1))

# jump on the spacebar key
keydown('space', p.jump)

def stop():
  p.act(DANCE_FRONT, -1)
  msg = text('Piggy\'s Revenge', color=WHITE).speed(0.1)
  msg.move_to((msg.x, -3), callback=msg.destroy)

p.move_to((12,12), callback=stop, animation=WALK_RIGHT)

def win():
   gameover(delay=3, exit=WIN)
callback(win, 20)
