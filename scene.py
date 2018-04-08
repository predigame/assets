WIDTH = 20
HEIGHT = 15
TITLE = 'Hello Porter'

background('bg2')

image('ground1', pos=(0,14))
for x in range(1, 19, 1):
   image('ground2', pos=(x, 14))
image('ground3', pos=(19,14))

image('house4', pos=(1, 10.65), size=6)
image('house1', pos=(12, 9.75), size=8)
image('wheel2', pos=(5,5), size=2).spin()

PIGH = 12
p = actor('Porter', pos=(-2,PIGH), size=2)

def jumpdone():
    p.speed(10)
    p.move_to((18,PIGH), callback=right_left, animation=RUN_RIGHT)

def jumpit():
    p.speed(5)
    p.move_to((10,6),(10,PIGH), callback=jumpdone, animation=ATTACK_RIGHT)

def left_right():
    p.speed(10)
    p.move_to((10,PIGH), callback=jumpit, animation=RUN_RIGHT)

def right_left():
    p.speed(3)
    p.move_to((0, PIGH), callback=left_right, animation=WALK_LEFT)

left_right()

def flake():
   pos = rand_pos()
   s = shape(CIRCLE, WHITE, pos=(pos[0], -5), size=0.1)
   s.move_to((pos[0], HEIGHT+5), callback=s.destroy)
   s.collides(sprites(), s.destroy)

callback(flake, 0.1, FOREVER)
