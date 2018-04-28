Working with Assets
===================
Game assets are all the *things* that a player sees in a game. While mostly visual (artwork), assets can also include sounds and other cool special effects.

Let's have fun working with Assets!

Getting Started
----------
Let's get started by exploring all of the existing assets that are available for use in our game.

### backgrounds
These are static images that we can use as a background splash image in our game. If you have other background images that you'd like to use, be sure to save them in the `backgrounds` directory. Please note that background images must end with `jpg` or `png` as other types of files will not work in Predigame.

### images
These are all the image sprites that are available for use in the game. While most of these sprites are static, it is possible to add special effects to a sprite, like `spin`, and `pulse`. You can add your own images as well, by saving them in the `images` directory. Be sure to look for images with a **transparent** background as those will look the best in our game.

Want to learn more about image sprites? Visit the [Predigame Sprite Tutorial](http://predigame.io/examples/sprites/).

### actors
Predigame Actors are Sprites that perform certain **actions** - mostly in the form of animations that make a game more realistic. Actors can perform any number of actions (walk, run, jump, attack) of which are usually left up to the artist's design. Creating actors are quite a bit of work, so you'll want to use the assets that are included with Predigame instead of trying to find or even make your own.

Want to learn more about actors? Visit the [Predigame Actor Tutorial](http://predigame.io/examples/actors/).

Example 1: The Pacing Piggy
----------
This example will have an actor pace left to right and back across the screen. Using your text editor, you'll want to create a file named `pace.py`. Be sure to save this in the same directory that has all of your assets (i.e. it should be in the directory that also has the directories `backgrounds`, `images`, and `actors`).

Inside this file, we'll add the first three lines of our game:
```python
WIDTH = 20
HEIGHT = 15
TITLE = 'Hello Porter'
```
This will create a game window that is `20` grid blocks wide and `15` grid blocks high and add *Hello Porter* to the titlebar. Try adjusting the window size to a dimension that works well for your computer.

Now let's save and run the game by typing this line in the terminal:
```
pred pace.py
```
This isn't very interesting right now, but so long as a window opens, the code is working as expected!

Now, under the `TITLE` line, let's create our actor:
```python
p = actor('Porter', pos=(-2,12), size=2.5)
```
When Predigame loads actors, it will scan for a the actor file `Porter.pga` that is inside the `actors/` directory. The game platform adds the extension (`.pga`) for the file, so that's one less thing that we'll need to type.

This line also creates a variable `p` that we can use to *refer* to Porter later. Anytime we talk directly to Porter, we'll see `p.` in the code - just think of that as us saying *"Hey Porter, do this"*!

The final two parts of this code are the starting position and size of Porter. We're using GRID-X (WIDTH) of `-2` and GRID-Y (HEIGHT) of `12`. This means that Porter will start off the screen on the left hand side. The following figure illustrates grid coordinates in a game window below. The size of Porter is `2.5` times his original size. By default, Porter would only be the size of a single grid block, which can be a little small for our game.

![alt text](http://predicate.us/predigame/images/sprites_grid3.png "Predigame Grid Coordinates")

Now since Porter won't be in the *visible* part of the screen just yet, it doesn't make sense to run the code just yet. Let's add in some movements.

```python
def left_right():
    p.move_to((18,12), animation=WALK_RIGHT, callback=right_left)

def right_left():
    p.move_to((0, 12), animation=WALK_LEFT, callback=left_right)

left_right()
```

The way this code works is pretty simple. Look at the line `left_right()`, that's what is called first. This line is what we call a **function invocation** and it's python's way of saying "let's go and run the `def left_right():` line of code". Looking at the guts of the function, we'll see just one line:

```python
    p.move_to((18,12), animation=WALK_RIGHT, callback=right_left)
```
Since the line starts with `p.`, python is  saying "*Hey Porter...*". The command for Porter is to move from his current position to grid cell `(18,12)`. During this time, Porter will execute a `WALK_RIGHT` animation as he moves in the right direction to the target point. As soon as he arrives, python will then execute another **callback function invocation** to this time to the `right_left` function.

Now looking at the guts of the `right_left()` function, we'll also see just one line:

```python
    p.move_to((0, 12), animation=WALK_LEFT, callback=left_right)
```
This code basically performs the opposite movement, and as soon as Porter returns to point `(0, 12)` the process will repeat.

Following the logic of the `right_left` and `left_right` callbacks, we'll basically see that Porter will pace left and right indefinitely. Now, let's try running the code and confirm that Porter paces left and right - and does so like the Energizer Piggy!

```
pred pace.py
```

### experimentation nuggets
Now that we have a pacing Porter, let's try some cool experiments:

**swap animations**
* Try swapping `WALK_LEFT` with `WALK_RIGHT` and `WALK_RIGHT` with `WALK_LEFT` for a little moon walking effect.
* Instead of walking, try a different animation. Here's a full listing of [available animations](https://github.com/predigame/predigame/blob/master/predigame/constants.py#L40).  Keep in mind that an actor may not support *every animation*, so it's good to check first to see what animations an actor supports. To list the supporting actions, add this line and look at the terminal for results. Keep in mind that these are strings, so instead of typing `attack_front` you'll want to use the constant `ATTACK_FRONT`.
	```
	print(p.get_actions())
	```
**walking up hill**
* Try changing the right_left coordinate from `(18,12)` to `(18,2)` and Porter will be a mountain climber.

**swap actors**
We've included all of our actor assets, so try giving another one of them a shot!  For example, try changing the line for `Porter` to `Zombie-4`
```python
p = actor('Zombie-4', pos=(-2,12), size=2.5)
```

**changing speeds**
Actors can have a movement speed. Try setting the speed prior each movement. Keep in mind, though, you'll want to vary the speeds otherwise it'll be hard to notice the change.

Here's the full functions to illustrate the varying speeds. *You only need to add the two lines for speed*.
```python
def left_right():
    p.speed(8)
    p.move_to((18,12), animation=WALK_RIGHT, callback=right_left)

def right_left():
    p.speed(4)
    p.move_to((0, 12), animation=WALK_LEFT, callback=left_right)
```
**add a jump**
Let's change up the animation for right to left. Instead of running straight left, we'll have Porter stop and jump first. In order to do this, we'll need to break up our callback functions.
```python
def jumpdone():
    p.speed(10)
    p.move_to((18,12), animation=WALK_RIGHT, callback=right_left)

def jumpit():
    p.speed(5)
    p.move_to((10,6),(10,12), animation=ATTACK_FRONT, callback=jumpdone)

def left_right():
    p.speed(10)
    p.move_to((10,12), animation=WALK_RIGHT, callback=jumpit)

def right_left():
    p.speed(3)
    p.move_to((0, 12), animation=WALK_LEFT, callback=left_right)
```
Notice that we added new functions `jumpit` and `jumpdone`. We broke up the callback functions by having `left_right` only move halfway and then call `jumpit`, which has two positions (notice that only the y-coordinate changes). When Porter hits the ground, `jumpdone` is called and Porter then completes the movement to the right.

###  challenge problems

* Try adding a `Bee` actor that flies across the screen
* Try adding a `.spin()` to the end of one of the movements. Spin can take a delay and number of rotations. So instead of `.spin()`, try `.spin(0.25, 10)` for a 10 *really fast* rotations.

Example 2: Coding a Scene
----------
Let's start to assemble a scene in our game. It's possible to merge this code with the previous example, but we'll leave that as a challenge problem.

Create a new file `scene.py` and let's start coding!

**backgrounds**
```python
WIDTH = 20
HEIGHT = 15
TITLE = 'Scene Example'

background('bg2')
```

The first three lines are basically the same as the first example. This time, though, we add a background. This line in particular will load the file `bg2.png` in the `backgrounds/` directory.

In addition to using one of the existing backgrounds, there are a number of other ways to add a background.

You can have just a single color. Here is an example of a gray background.
```python
   background(GRAY)
```
If you have a particular color in mind, it's possible to also define the background with a `(red, green, blue)` tuple.
```python
   background((25, 25, 25))
```
We also have a pretty cool image service that will randomly pick and use a background from the Internet. This can add a little jazz to your scene.
```python
   background()
```
Try saving and running your game. Type the following command in the console.

```
pred scene.py
```
**ground tiles**
After you decide on a background, we'll add some ground tiles. To do this we're going to start by placing the left and right end-cap tiles first. Remember that computers always start counting at zero, so `(0,14)` and `(19,14)` represent the bottom left and right corners.
```python
image('ground1', pos=(0,14))
image('ground3', pos=(19,14))
```

Let's run our code to confirm that the `ground1` (or left) tile and `ground3` (or right) tile are showing up correctly. In order to fill in all of the in between tiles, we could have separate lines of code, but that would be a lot of typing. It's much easier to use a loop.
```python
for x in range(1, 19, 1):
   image('ground2', pos=(x, 14))
```
This loop will start counting at `1` and finish after `18`. Each number takes on a particular value. So looking at this loop, it would be the same if we were to write:

```python
image('ground2', pos=(1, 14))
image('ground2', pos=(2, 14))
...
# ... my fingers hurt from all this typing ...
image('ground2', pos=(2, 18))
```
But loops are so much better. It is always better to let the computer do all the hard work.

Let's try it out now. We're expecting to see a background as well as a fully placed set of ground tiles:

```
pred scene.py
```

**objects**

Now that we have a background splash as well as some grass for a ground, we'll extend our scene by adding some houses. Here's two lines of code that will place a house on the left and right sides of our scene.

```python
image('house4', pos=(1, 10.65), size=6)
image('house1', pos=(12, 9.75), size=8)
```
*Keep in mind* - if you don't specify a size, the image will appear in a single grid cell.

Need help aligning images? I may be useful to enable the drawing grid with the following line:

```python
grid()
```
Now go ahead and try placing some other sprites to complete the scene!

**snowing effect**
Snow?!? Yes! Let's try adding a snow effect to our scene!
```python
def flake():
   pos = rand_pos()
   s = shape(CIRCLE, WHITE, pos=(pos[0], -5), size=0.1)
   s.move_to((pos[0], HEIGHT+5), callback=s.destroy)

callback(flake, 0.05, FOREVER)
```
Here's how our snow flakes work. We first define the function `flake()` that contains the three lines of code for making snow. Inside these three lines we first create a random position - it can be *anywhere* in our game canvas, but we are only interested in the X-coordinate - meaning that we only care about the left and right position of the flake. This is because all flakes start off the top of the screen `pos=(pos[0], -5)` and then move down to `(pos[0], HEIGHT+5)` which falls off the bottom of the screen. The code fragment `pos[0]` basically means we just want the x coordinate. If we used `pos[1]`, that would give us the y coordinate.

The callback function will generate a new flake every `0.05` seconds (that's a lot of flakes!) and repeat this call `FOREVER`!

Example 3: Piggy Combat
----------
The Zombies are coming and Porter must defend himself! Here's a complete game that will exercise some pretty cool Predigame features. Specifically, we'll cover:

* Functions and Callbacks - timer and collision
* Actor Actions
* Killing Things
* Basic Gravity and Jumping
* Keeping Score

### Getting Started

Let's get started by creating a new file `combat.py` and add our standard three lines of code:

```python
WIDTH = 20
HEIGHT = 15
TITLE = 'Piggy Combat'
```

Now let's define some ground tiles that will cover the bottom of the game canvas:

```python
image('ground1', pos=(0,14))
for x in range(1, 19, 1):
   image('ground2', pos=(x, 14))
image('ground3', pos=(19,14))
```

Let's try to save and run our code. Not much to see just yet, but do confirm we have some ground tiles! You can run the game by typing the following line in your terminal:

```python
pred combat.py
```
Now, we need to add Porter.  This is a short hand notation for creating an actor, assigning a mass, and then activating Porter's movements with the arrow keys.

```python
p = actor('Porter', pos=(2,0), size=3).mass(10).keys()
```

Mass is a new concept. Things that have a mass will need to obey the rules of gravity.  Try to save and run our code. You'll notice that Porter falls to the top of the grass tiles. We make Porter of size 3 - feel free to change tweak the size, but it will need to be a whole number (no decimal points).

### Jump and Attack Callbacks

Now that Porter has been added to the game we can add keyboard callback functions that will allow us to introduce jump and attack actions.

Here's the line for allowing Porter to jump (activated with space bar key):
```python
keydown('space', p.jump)
```

And now the attack (activated with return/enter key):
```python
keydown('return', partial(p.act, ATTACK, 1))
```

We'll also need to register the game reset key, especially for the next step!
```python
keydown('r', reset)
```

Give these changes a shot!

### Adding Enemies!

This example function will create a zombie every six seconds, from the right and walking to the left.  Make sure you jump over those zombies. You won't survive contact with them!

Add the following code to the bottom of your game:

```python
def hit(enemy, porter):
      porter.kill()

def right():
   e = actor('Zombie-5', pos=(22,12.15), size=2)
   e.speed(1)
   e.move_to((-2, 12.15), animation=WALK_LEFT, callback=e.destroy)
   e.collides(p, hit)

callback(right, 6, FOREVER)
```
Give these changes a shot! Feel free to swap out the enemy actor as well as adjust the size and the speed.

Having fun yet? Try making the game more complicated by adding more enemies from the left.

```python
def left():
   e = actor('Zombie-8', pos=(-2,12.15), size=2).flip()
   e.speed(1)
   e.move_to((22, 12.15), animation=WALK_RIGHT, callback=e.destroy)
   e.collides(p, hit)

callback(left, 6, FOREVER)
```
Again, try giving swapping out actors and as well as adjusting the size and speed.

### Fighting Back
Our Porter can't do much just yet and just jumping over the zombies can get a little boring. Let's have Porter take out the zombies with his super strong punch.

*This code will replace your existing attack function.* **Make sure you delete it!**

```python
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
```
We've added some comments in the function to describe the three possible conditions of a zombie collision:

1. The zombie is walking `RIGHT` and Porter attacks from the `LEFT`
	* The Zombie Dies!
2. The zombie is walking `LEFT` and Porter attacks from the `RIGHT`
	* The Zombie Dies!
3. Zombie hits a defenseless Porter
	* Our Piggy Dies!

Try giving this change a shot.

### Whacky Randomness
We really change up the dynamics of our game by adding some randomness! To do this, there is a special function in Predigame called `randint` that takes two numbers and randomly pics a number in that range. We can use randoms for size, speed, and launch variability.

Look for the line starting with `e.speed` and change to the following. This will change any of the enemies speeds.
```python
e.speed(randint(1,5))
```
Want more enemies? Try adjusting the timer callbacks to the following (can also be applied to left side):
```python
callback(right, randint(3,6), FOREVER)
```

### Adding a background scene
Let's try adding some things to the background to make the game look a little more pleasing to the eye. Here are some examples of things that can be added, but you can add anything you want from the `images/` directory.

```python
# use a background image
background('bg2')

# create houses in the background (they will not interfere with the player)
background(image('house4', pos=(1, 10.65), size=6))
background(image('house1', pos=(12, 9.75), size=8))

# a fence where Porter can jump and get away from the zombies
for x in range(3):
   image('crate1', pos=(x+8, 10), tag=OBSTACLE)
```

Notice that everything, but the fence, is wrapped in a `background()` function. So these sprites don't participate in the game - they are just for presentation.

What can you do with the crate?

### Keeping Score
We're going to add two different types of scoring options in the game:
* *kill counter* - achieve the greatest number of kills
* *duration counter* - survive the longest amount of time

#### Kill Counter
**Step 1**: Scorebox Registration
Add the following code the bottom of your file:
```python
score(prefix='Kills: ', pos=LOWER_RIGHT)
```
**Step 2**: Tally the Kills
Add the following code to `hit(enemy, porter)` function. Not that this is not complete code. You'll want to add the `score` line under each `enemy.kill()`:

```python
score(1, pos=LOWER_RIGHT)
```
A completed `hit(enemy, porter)` with scoring enabled will look like this:

```python
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
```

#### Duration Counter
This is a really easy counter that can be added without too much work. Just add the following line to the bottom of your code file:

```python
stopwatch(prefix='Survival: ')
```
### Falling Blades of Death
In addition to needing to defined yourself from a continuous stream of enemies, you can also add falling saw blades of death. This works a little like snow, but a little more deadly.

```python
# a callback when the player is hit by a blade
def die(blade, porter):
   if porter.health > 0:
       porter.kill()
       text('game over')
       gameover()

# falling blades of death
def fall():
   pos = rand_pos()
   b = image('saw', pos=(pos[0], -5), size=1)
   b.speed(randint(1,6))
   b.move_to((pos[0], HEIGHT+5), callback=b.destroy)
   b.collides(p, die)
callback(fall, randint(1, 5), FOREVER)
```
### Fun Ways to Die
When a saw blade hits Porter, the game executes a `porter.kill()` line. Try this little mod:

```python
def die(blade, porter):
   if porter.health > 0:
       porter.spin(0.25).move_to((porter.pos[0], HEIGHT), animation=DIE_FRONT, callback=porter.kill)
       text('game over')
       gameover(10)
```
Can you add your own fun way to die? How about a blood splatter?

### Bullets!
Bullets may not be the right term since Porter doesn't have a weapon, but these are pretty fun to watch and devastating for the enemy.

```python
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
      # make sure we don't shoot ourselves!
      actors = get(x)
      if a in actors:
        actors.remove(a)
      b.collides(actors, shot)
keydown('s', partial(shoot, p, ['enemy', 'bat']))
```

The `s` key triggers the throw. What happens when you tweak the speed? Try replacing the bullet with an image.

### Building
This code allows us to build and destroy blocks on the fly!

```python
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
```
Try swapping out the image. What happens if you destroy the ground sprites?

#### Monitoring the "death jump"
By default the game doesn't know anything about the "ground". Here's a simple way to confirm if Porter makes a "death jump":

```python
# check for falling to death events
def monitor():
  if p.y >= HEIGHT+5:
    text('bye bye baby')
    gameover()
callback(monitor, 2, FOREVER)
```

### Bats!

In addition to falling blades, here's a fun way to have pesky bats fly in to Porter's position.

```python
# bats fly in
def flyin():
   y = rand_pos()[1]
   x = choice([-5, WIDTH+5])
   e =  actor('Bat', pos=(x,y), size=2, tag='bat')
   e.speed(1)
   e.move_to(p.pos, animation=FLY_FRONT, callback=e.destroy)
   e.collides(p, die)
   callback(flyin, randint(3,7))
callback(flyin, randint(3,7))
```

Notice we recycle the `die` function? That's one of the cool things you can do with functions. They make our code reusable.





### General Challenge Problems

#### Build a crate stairway to heaven
The following code adds a few crates for Porter to jump up and avoid a stream of zombies.

```python
for x in range(5):
   image('crate1', pos=(x, 11), tag=OBSTACLE)
```
*How do you arrange crates (think many for loops) to reach the top of the screen?*

#### Add effects to the saw blades?

Try adding a `.spin()` or a `.pulse()` to the falling blades. Need more help with effects? Checkout the [this tutorial](http://predigame.io/examples/sprites/#sprite-effects) on the Predigame Website.

#### Hacking Jumps
Take a look at this pretty uninteresting line of code:

```python
keydown('space', p.jump)
```

Porter jumps anytime a spacebar is hit. It's pretty easy to change the behavior of jump by adding a `partial` and the passing in a few parameters.

**THE HIGH JUMP**
```python
keydown('space', partial(p.jump,height=10))
```   
**THE LONG JUMP**
```python
keydown('space', partial(p.jump,arc=[5,5,5,5,5,5,5,5,5]))
```   
How do you combine them? How do you register different types of jumps to different keyboard keys?

#### The Annoying Bee [HARD]

Try adding in a Bee actor that follows Porter around. The Bee doesn't have to attack, but should fly around Porter.
**HINT:** You'll need to use something like the `monitor` function to check and move the Bee.
