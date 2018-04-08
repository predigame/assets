WIDTH = 20
HEIGHT = 15
TITLE = 'Hello Porter'

p = actor('Porter', pos=(-2,12), size=2.5)

print(p.get_actions())

def left_right():
    p.move_to((18,12), animation=WALK_RIGHT, callback=right_left)

def right_left():
    p.move_to((0, 12), animation=WALK_LEFT, callback=left_right)

left_right()
