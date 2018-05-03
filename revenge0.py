# a window 20 grid blocks wide by 15 grid height
WIDTH = 20
HEIGHT = 15

# title of the window
TITLE = 'Piggy Revenge'

# use a background image
background('bg2')

# ground tiles
image('ground1', pos=(0,14), tag=OBSTACLE)
for x in range(1, 19, 1):
   image('ground2', pos=(x, 14), tag=OBSTACLE)
image('ground3', pos=(19,14), tag=OBSTACLE)

## create houses in the background (they will not interfere with the player)
background(image('house4', pos=(1, 10.65), size=6))
background(image('house1', pos=(12, 9.75), size=8))

# a crate where Porter can jump and get away from the zombies
for x in range(3):
    image('crate1', pos=(x+8, 11), tag=OBSTACLE)
for x in range(2):
    image('crate1', pos=(x+12, 8), tag=OBSTACLE)
for x in range(2):
    image('crate1', pos=(x+8, 6), tag=OBSTACLE)
for x in range(2):
    image('crate1', pos=(x+12, 4), tag=OBSTACLE)
for x in range(2):
    image('crate1', pos=(x+8, 2), tag=OBSTACLE)
for x in range(5):
    image('crate1', pos=(x, 2), tag=OBSTACLE)

# create Porter, give him a mass so he falls down, use arrow keys to move left/right
p = actor('Porter', pos=(0,-3), size=2, tag='Porter').mass(10).keys()

# throw a punch on the return/enter key
keydown('return', partial(p.act, ATTACK, 1))

# jump on the spacebar key
keydown('space', p.jump)

# stopwatch
stopwatch(prefix='Survival: ')

# kill counter
score(prefix='Kills: ', pos=LOWER_RIGHT)

# press 'r' key to restart game
keydown('r', reset)
