WIDTH = 31
HEIGHT = 19
TITLE = 'Zombie Madness'

background()

player = actor('Porter', (1, HEIGHT-2), size=2, tag='player', abortable=True)
player.speed(5).keys(precondition=player_physics)

txt = text("TIME TO DIE!!")
callback(txt.destroy, 4)

def hit(enemy, player):
   player.spin()
   player.kill()
   enemy.stop()
   enemy.act(ATTACK, FOREVER)
   text('this little piggy is delicious')
   gameover(delay=10, exit=LOSE)

def win():
   text('bacon shortage. you win!')
   gameover(delay=5, exit=WIN)


red = actor('Zombie-'+str(randint(1,10)), (WIDTH+15,5), tag='red', size=15).speed(8)
red.collides(player, hit)
points = [(p, 5) for p in range(WIDTH+15, -25, -2)]
red.move_to(*points, callback=win)
keydown('r', reset)
