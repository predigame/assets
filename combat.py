# edit ideas
# 1. change scene
# 2. change characters
# 3. change speed and rates (make them random)
# 4. add score

# a window 20 grid blocks wide by 15 grid height
WIDTH = 20
HEIGHT = 15

# title of the window
TITLE = 'Piggys Revenge'

# use a background image
background('bg2')

# ground tiles
image('ground1', pos=(0,14))
for x in range(1, 19, 1):
   image('ground2', pos=(x, 14))
image('ground3', pos=(19,14))

# create houses in the background (they will not interfere with the player)
background(image('house4', pos=(1, 10.65), size=6))
background(image('house1', pos=(12, 9.75), size=8))

# a fence where Porter can jump and get away from the zombies
for x in range(3):
   image('fence5', pos=(x+8, 10))

# create Porter, give him a mass so he falls down, use arrow keys to move left/right
p = actor('Porter', pos=(2,11.75), size=2).mass(10).keys()

# throw a punch on the return/enter key
keydown('return', partial(p.act, ATTACK, 1))

# jump on the spacebar key
keydown('space', p.jump)

# when an enemy hits the Porter
def hit(enemy, porter):
   # enemy is moving right and Porter is punching from the left
   if enemy.direction == RIGHT and porter.action == ATTACK_LEFT:
      enemy.kill()
   # enemy is moving left and Porter is punching from the right
   elif enemy.direction == LEFT and porter.action == ATTACK_RIGHT:
      enemy.kill()
   # the enemy is alive but Porter didn't act. he dies!
   elif enemy.health > 0:
      enemy.kill()

# create an enemy from the left. move right.
def left():
   e = actor('Zombie-8', pos=(-2,12.15), size=2).flip()
   e.speed(1)
   e.move_to((22, 12.15), animation=WALK_RIGHT, callback=e.destroy)
   e.collides(p, hit)

# create an enemy from the right. move left.
def right():
   e = actor('Zombie-3', pos=(22,12.15), size=2)
   e.speed(1)
   e.move_to((-2, 12.15), animation=WALK_LEFT, callback=e.destroy)
   e.collides(p, hit)

# callback to create enemies
callback(right, 6, FOREVER)
callback(left, 6, FOREVER)

# press 'r' key to restart game
keydown('r', reset)
