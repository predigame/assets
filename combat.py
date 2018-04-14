# a window 20 grid blocks wide by 15 grid height
WIDTH = 20
HEIGHT = 15

# title of the window
TITLE = 'Piggy Combat'

# ground tiles
image('ground1', pos=(0,14))
for x in range(1, 19, 1):
   image('ground2', pos=(x, 14))
image('ground3', pos=(19,14))

# create Porter, give him a mass so he falls down, use arrow keys to move left/right
p = actor('Porter', pos=(2,0), size=3).mass(10).keys()

# throw a punch on the return/enter key
keydown('return', partial(p.act, ATTACK, 1))

# jump on the spacebar key
keydown('space', p.jump)

# press 'r' key to restart game
keydown('r', reset)
