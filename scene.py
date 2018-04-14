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

def flake():
   pos = rand_pos()
   s = shape(CIRCLE, WHITE, pos=(pos[0], -5), size=0.1)
   s.move_to((pos[0], HEIGHT+5), callback=s.destroy)
   s.collides(sprites(), s.destroy)

callback(flake, 0.1, FOREVER)
