# spin enemies
# - keep score (hits, survival time, health)
# - falling saw blades of death
# - wacky jumps
# - duration goal
# - throw something at zombies
# have zombies fall out of the sky
# golden star reward
# - make the piggy fall and die (fun ways to die)
# hostage
# goal coins
# levels
# vary _health
# complex obstacles
# build and destroy to get a goal
# pitfalls
# moving floors

# a window 20 grid blocks wide by 15 grid height
WIDTH = 20
HEIGHT = 15

# title of the window
TITLE = 'Piggy Combat'

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
      print('{} ==> {}'.format(e.pos, e.action))
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
#def move_right(e):
#   print('move_right')
#   if e.pos[0] > WIDTH-2:
#      e.destroy()
#   else:
#      e.move_to((WIDTH-2, e.pos[1]), animation=WALK_RIGHT)
#      callback(partial(monitor, e, partial(move_right, e)), 0.75)

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

# make saw blades fall
def die(blade, porter):
   if porter.health > 0:
       porter.spin(0.25).move_to((porter.pos[0], HEIGHT), animation=DIE_FRONT, callback=porter.kill)
       text('game over')
       gameover()

def fall():
   pos = rand_pos()
   b = image('saw', pos=(pos[0], -5), size=1)
   b.speed(randint(1,6))
   b.move_to((pos[0], HEIGHT+5), callback=b.destroy)
   b.collides(p, die)
#callback(fall, randint(1, 5), FOREVER)


# stopwatch
stopwatch(prefix='Survival: ')
score(prefix='Kills: ', pos=LOWER_RIGHT)

# press 'r' key to restart game
keydown('r', reset)

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

# build and destroy crates
def build(x,y):
   s = image('crate1', (p.x+x, p.y+y), tag=OBSTACLE, order=BACK)
def destroy():
   next_area = to_area(p.x, p.y, p.width, p.height, bottom_only=True)
   for a in next_area:
      b = at((a[0],a[1]+1))
      if b is not None:
         if isinstance(b, Sprite):
            b.destruct(0)
         else:
            for c in b:
                c.destruct(0)
keydown('1', partial(build, -1, 2))
keydown('2', partial(build, 1, 2))
keydown('q', destroy)
keydown('w', destroy)

# check for falling to death events
def monitor():
  if p.y >= HEIGHT+5:
    text('bye bye baby')
    gameover()
callback(monitor, 2, FOREVER)

# bats fly in
def flyin():
   y = rand_pos()[1]
   x = choice([-5, WIDTH+5])
   e =  actor('Bat', pos=(x,y), size=2, tag='bat')
   e.speed(1)
   e.move_to(p.pos, animation=FLY_FRONT, callback=e.destroy)
   e.collides(p, die)
   callback(flyin, randint(3,7))
#callback(flyin, randint(3,7))
