# Subject: Making Break-Out game: ball movement
# visit here: 
# https://elgoog.im/breakout/

# let's think about what we have to do
# - ball is moving --> we need a variable for that. 

x = 0 # ball's x position

def setup():
  size(800, 600)
  global x
  x = 0

def draw():
  #background(200)
  global x
  ellipse(x, 100, 50, 50)
  x = x + 1

# Mission: 
# - change the ball color
