# a window 20 grid blocks wide by 15 grid height
WIDTH = 25
HEIGHT = 15

# title of the window
TITLE = 'Piggy Revenge'

# use a background image
background()

# ground tiles
image('ground1', pos=(0,14), tag=OBSTACLE)
for x in range(1, WIDTH-1, 1):
   image('ground2', pos=(x, 14), tag=OBSTACLE)
image('ground3', pos=(WIDTH-1,14), tag=OBSTACLE)

# create Porter, give him a mass so he falls down, use arrow keys to move left/right
p = actor('Porter', pos=(0,-3), size=2, tag='Porter').mass(10).keys()

# throw a punch on the return/enter key
keydown('return', partial(p.act, ATTACK, 1))

# jump on the spacebar key
keydown('space', p.jump)

# stopwatch
stopwatch(prefix='Survival: ')

# countdown timer
def notime():
   text("out of time")
   p.kill()
   gameover()
#timer(20, pos=LOWER_LEFT, callback=notime)

# kill counter
score(prefix='Kills: ', pos=LOWER_RIGHT)

# press 'r' key to restart game
keydown('r', reset)

# check for falling to death events
def monitor():
    if p.y >= HEIGHT+5:
        text('bye bye baby')
        gameover()
callback(monitor, 2, FOREVER)

# death event
def die(thing, victim):
   if victim.health > 0:
       victim.kill()
       if victim in get('player'):
           text('game over')
           gameover()
       else:
           score(1, pos=LOWER_RIGHT)
