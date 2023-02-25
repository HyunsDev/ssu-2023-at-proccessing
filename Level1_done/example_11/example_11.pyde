# Subject: Making Break-Out game: ball bouncing
# - conditional statement: if statement

# what we have to to? --> we need another variable to keep ball's direction
x = 100 #ball's x position
xdir = 4 #ball’s direction
diam = 50 #ball’s diameter

def setup():
    size(800, 600)

def draw():
    global x, xdir, diam
    background(200)
    ellipse(x, 100, diam, diam)
    x = x + xdir
    
    if x + diam/2  > width: #system variable of processing
        xdir = xdir * -1;
  
    if x - diam/2 < 0:
        xdir = xdir * -1;

# Mission: change ball color when it hits the boundary
# - touch the right boundary: make it yellow
# - touch the left boundary: make it blue
