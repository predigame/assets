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


# when an enemy hits the Porter
def hit(enemy, porter):
   # don't do anything when the enemy is dead
   if enemy.health == 0:
      return
   # enemy is moving right and Porter is punching from the left
   if enemy.direction == RIGHT and porter.action == ATTACK_LEFT:
      enemy.kill()
      score(1, pos=LOWER_RIGHT)
   # enemy is moving left and Porter is punching from the right
   elif enemy.direction == LEFT and porter.action == ATTACK_RIGHT:
      enemy.kill()
      score(1, pos=LOWER_RIGHT)
   # the enemy is alive but Porter didn't act. he dies!
   else:
      porter.kill()
      text('game over')
      gameover()

def emonitor():
   for e in get('enemy'):
      if e.action.startswith(DIE) and e.health == 0:
         e.destruct(1.5)
         continue
      if e.action.startswith(IDLE):
         e.move_to((e.attributes['destination'], e.y))
      elif randint(1,4) == 2:
         e.jump()
      elif randint(1,5) == 2:
         e.stop()
         shoot(e, ['Porter', 'enemy', 'bat'])
      if e.y >= HEIGHT:
         e.kill()
callback(emonitor, 0.5, FOREVER)

# create an enemy from the left. move right.
def left():
   e = actor('Zombie-8', pos=(0,0), size=2, tag='enemy').flip()
   e.mass(10)
   e.speed(1)
   e.attributes['destination'] = 22
   e.move_to((22, 0), animation=WALK_RIGHT)
   e.collides(p, hit)
callback(left, 6, FOREVER)

# create an enemy from the right. move left.
def right():
   e = actor('Zombie-3', pos=(WIDTH-1,12.15), size=2, tag='enemy')
   e.speed(1)
   e.mass(10)
   e.attributes['destination'] = -2
   e.move_to((-2, 12.15), animation=WALK_LEFT)
   e.collides(p, hit)
callback(right, 6, FOREVER)

# shoot a bullet
def shot(bullet, victim):
   if victim.health > 0:
       score(1, pos=LOWER_RIGHT)
       victim.kill()
       bullet.destroy()

def shoot(a, tags):
   a.act(ATTACK,1)
   b = shape(CIRCLE, YELLOW, pos=(a.x+0.75, a.y+1), size=0.2)
   b.speed(10)
   b.move_to((a.facing()[0], (a.y+1)), callback=b.destroy)
   for x in tags:
      actors = get(x)
      if a in actors:
        actors.remove(a)
      b.collides(actors, shot)
keydown('s', partial(shoot, p, ['enemy', 'bat']))

# check for falling to death events
def monitor():
  if p.y >= HEIGHT+5:
    text('bye bye baby')
    gameover()
callback(monitor, 2, FOREVER)
