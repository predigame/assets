WIDTH = 20
HEIGHT = 15
TITLE = 'Piggy Combat'

# use a background image
background('bg2')

# ground tiles
image('ground1', pos=(0, HEIGHT-1), tag=OBSTACLE)
image('ground3', pos=(WIDTH-1, HEIGHT-1), tag=OBSTACLE)
for x in range(1, WIDTH-1, 1):
    image('ground2', pos=(x, HEIGHT-1), tag=OBSTACLE)

# background scene
background(image('house4', pos=(1, 10.65), size=6))
background(image('house1', pos=(12, 9.75), size=8))

# a crate where Porter can jump and get away from the zombies
for x in range(5):
   image('crate1', pos=(x, 11), tag=OBSTACLE)

# create our porter!
p = actor('Porter', pos=(2, 0), size=2).mass(10).keys()

# spacebar jumps
keydown('space', p.jump)

# return/enter throws a punch
keydown('return', partial(p.act, ATTACK, 1))

# r to reset
keydown('r', reset)

# when an enemy hits the Porter
def hit(enemy, porter):
   # don't do anything when the enemy is dead
   if enemy.health == 0:
      return
   # enemy is moving right and Porter is punching from the left
   if enemy.direction == RIGHT and porter.action == ATTACK_LEFT:
      enemy.kill()
   # enemy is moving left and Porter is punching from the right
   elif enemy.direction == LEFT and porter.action == ATTACK_RIGHT:
      enemy.kill()
   # the enemy is alive but Porter didn't act. he dies!
   else:
      porter.kill()
      text('game over')
      gameover()

def right():
    e = actor('Zombie-5', pos=(22, 12.15), size=2)
    e.frame_rate = 2
    e.speed(randint(1,5))
    e.move_to((-2, 12.15), animation=WALK_LEFT, callback=e.destroy)
    e.collides(p, hit)
callback(right, randint(3,6), FOREVER)

def left():
    e = actor('Zombie-8', pos=(-2, 12.15), size=2)
    e.frame_rate = 2
    e.speed(randint(1,5))
    e.move_to((22, 12.15), animation=WALK_RIGHT, callback=e.destroy)
    e.collides(p, hit)
callback(left, randint(3,6), FOREVER)
