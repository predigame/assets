WIDTH = 20
HEIGHT = 15

# title of the window
TITLE = 'Piggy Combat'

# use a background image
background('bg2')

####
####
####
####
#for x in range(HEIGHT):
#   for y in range(WIDTH):
#      image('crate1', pos=(x,y), tag=OBSTACLE)

#
##
###
####
#####
#for x in range(0, HEIGHT, 1):
#   for y in range(x, HEIGHT, 1):
#      image('crate1', pos=(x,y), tag=OBSTACLE)

#######
# #####
#  ####
#   ###
#    3#
#     #
#for x in range(0, HEIGHT, 1):
#   for y in range(0, x+1, 1):
#      image('crate1', pos=(x+5,y), tag=OBSTACLE)

#     #
#    ##
#   ###
# #####
#######
#for x in range(HEIGHT, 0, -1):
#   for y in range(HEIGHT, HEIGHT-x, -1):
#      print(x,y)
#      image('crate1', pos=(x+4,y-1), tag=OBSTACLE)

######
#####
####
###
##
#
#for x in range(0, HEIGHT, 1):
#   for y in range(0, HEIGHT-x, 1):
#      print(x,y)
#      image('crate1', pos=(x,y), tag=OBSTACLE)

#     #
#    ###
#   #####
#  #######
# #########
############
for x in range(HEIGHT, 0, -1):
   for y in range(x, HEIGHT-x, -1):
      image('crate1', pos=(y-1,x-1), tag=OBSTACLE)


# create Porter, give him a mass so he falls down, use arrow keys to move left/right
p = actor('Porter', pos=(0,-3), size=2, tag='Porter').mass(10).keys()
keydown('space', p.jump)
