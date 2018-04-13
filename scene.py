WIDTH = 20
HEIGHT = 15
TITLE = 'Hello Porter'

background('bg2')

image('ground1', pos=(0,14))
for x in range(1, 19, 1):
   image('ground2', pos=(x, 14))
image('ground3', pos=(19,14))

#image('house4', pos=(1, 10.65), size=6)
#image('house1', pos=(12, 9.75), size=8)
#image('wheel2', pos=(5,5), size=2).spin()

def flake():
   pos = rand_pos()
   s = shape(CIRCLE, WHITE, pos=(pos[0], -5), size=0.1)
   s.move_to((pos[0], HEIGHT+5), callback=s.destroy)
   s.collides(sprites(), s.destroy)

callback(flake, 0.1, FOREVER)

def attack(p):
   p.act(ATTACK, 1)

p = actor('Porter', pos=(2,11.75), size=2)
p.mass(5)
p.keys()
keydown('return', partial(attack, p))
keydown('space', p.jump)

def hit(e, p):
   if e.direction == RIGHT and p.action == ATTACK_LEFT:
      e.kill()
   elif e.direction == LEFT and p.action == ATTACK_RIGHT:
      e.kill()
   elif e.health > 0:
      p.kill()

def left():
   e = actor('Zombie-8', pos=(-2,12.15), size=2).flip()
   e.speed(randint(1,3))
   e.move_to((22, 12.15), animation=WALK_RIGHT, callback=e.destroy)
   e.collides(p, hit)

def right():
   e = actor('Zombie-3', pos=(22,12.15), size=2)
   e.speed(randint(1,3))
   e.move_to((-2, 12.15), animation=WALK_LEFT, callback=e.destroy)
   e.collides(p, hit)

callback(right, randint(3,5), FOREVER)
callback(left, randint(3,5), FOREVER)
keydown('r', reset)
