# Subject: Making Break-Out game: let's make it on 2D space

# what we have to do? --> we need new variables for y coordinate

x = 100 #ball's x position
y = 100
xdir = 4 #ball’s direction
ydir = 4
diam = 50 #ball’s diameter

def setup():
    size(800, 600)

def draw():
    global x, y, xdir, ydir, diam
    background(200)
    ellipse(x, y, diam, diam)
    x = x + xdir
    y += ydir
    
    if x + diam/2  > width:
        xdir = xdir * -1;
        fill(255, 0, 0);
  
    if x - diam/2 < 0:
        xdir = xdir * -1;
        fill(255, 255, 0);
        
    if y - diam/2 < 0:
        ydir = ydir * -1;
  
    if y + diam/2 > height:
        ydir = ydir * -1;

# Mission: change ball color
