For Loop Challenge
===================
Test your mad coding skills with the For Loop Challenge

Getting Started
----------
Let's get started by creating a basic game in a file named `forloop.py`.

```python
WIDTH = 20
HEIGHT = 15

# title of the window
TITLE = 'For Loop Challenge'

# use a background image
background('bg2')
```
Basic Nested Loop
----------
Nested loops can be used magnify the number of times we need to perform a particular task. Take, for instance, the following code:

```python
for x in range(HEIGHT):
   for y in range(WIDTH):
      image('crate1', pos=(x,y), tag=OBSTACLE)
```

In our game, it will create the following block arrangement:

![alt text](http://predicate.us/predigame/images/forloop1.jpg "loop 1")

Challenge 1
----------
Challenge 1 is a freebee. This code builds a basic triangle. Look at how the `for y in` starts with `x` - a variable. Run the numbers through your end or simply loop at how they repeat in the console.

```python
for x in range(0, HEIGHT, 1):
   for y in range(x, HEIGHT, 1):
      print(x,y)
      image('crate1', pos=(x,y), tag=OBSTACLE)
```      
![alt text](http://predicate.us/predigame/images/forloop2.jpg "loop 2")

Challenge 2
----------
![alt text](http://predicate.us/predigame/images/forloop3.jpg "loop 3")

Challenge 3
----------------

![alt text](http://predicate.us/predigame/images/forloop4.jpg "loop 4")

Challenge 4
--------------

![alt text](http://predicate.us/predigame/images/forloop5.jpg "loop 5")

Challenge 5 (REALLY HARD)
--------------
![alt text](http://predicate.us/predigame/images/forloop6.jpg "loop 6")
