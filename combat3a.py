WIDTH = 20
HEIGHT = 15
TITLE = 'Piggy Combat'

background('bg2')

image('ground1', pos=(0, HEIGHT-1), tag=OBSTACLE)
image('ground3', pos=(WIDTH-1, HEIGHT-1), tag=OBSTACLE)
for x in range(1, WIDTH-1, 1):
    image('ground2', pos=(x, HEIGHT-1), tag=OBSTACLE)

background(image('house4', pos=(1, 10.65), size=6))
background(image('house1', pos=(12, 9.75), size=8))

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


p = actor('Porter', pos=(2, 0), size=2).mass(10).keys()

keydown('space', p.jump)

keydown('s', partial(p.jump, height=2, arc=[5,5,5]))

keydown('return', partial(p.act, ATTACK, 1))

keydown('r', reset)

def hit(enemy, porter):
    if enemy.health == 0:
       return
    if enemy.direction == RIGHT and porter.action == ATTACK_LEFT:
        score(1, pos=LOWER_RIGHT)
        enemy.kill()
    elif enemy.direction == LEFT and porter.action == ATTACK_RIGHT:
        score(1, pos=LOWER_RIGHT)
        enemy.kill()
    else:
        porter.kill()
        text('game over')
        gameover()

def right():
    e = actor('Zombie-5', pos=(22, 12.15), size=2, tag='enemy')
    e.frame_rate = 2
    e.speed(randint(1,5))
    e.move_to((-2, 12.15), animation=WALK_LEFT, callback=e.destroy)
    e.collides(p, hit)
callback(right, randint(3,6), FOREVER)

def left():
    e = actor('Zombie-8', pos=(-2, 12.15), size=2, tag='enemy')
    e.frame_rate = 2
    e.speed(randint(1,5))
    e.move_to((22, 12.15), animation=WALK_RIGHT, callback=e.destroy)
    e.collides(p, hit)
callback(left, randint(3,6), FOREVER)

score(prefix='Kills: ', pos=LOWER_RIGHT)
stopwatch(prefix='Survival: ', pos=LOWER_LEFT)

# falling blades of death
def die(blade, porter):
    if porter.health > 0:
       porter.spin(0.25).move_to((porter.pos[0], HEIGHT), animation=DIE_FRONT, callback=porter.kill)
       text('game over')
       gameover(10)

def fall():
    pos = rand_pos() # x = pos[0], y = pos[1]
    b = image('saw', pos=(pos[0], -5), size=1)
    b.spin(0.25)
    b.speed(randint(1,6))
    b.move_to((pos[0], HEIGHT+5), callback=b.destroy)
    b.collides(p, die)
callback(fall, randint(1,5), FOREVER)

# shoot a bullet
def shot(bullet, victim):
    if victim.health > 0:
       score(1, pos=LOWER_RIGHT)
       victim.kill()
       bullet.destroy()

def shoot(a, tags):
    a.act(ATTACK, 1)
    b = shape(CIRCLE, YELLOW, pos=(a.x+0.75, a.y+1), size=0.2)
    b.speed(10)
    b.move_to((a.facing()[0], a.y+1), callback=b.destroy)
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

