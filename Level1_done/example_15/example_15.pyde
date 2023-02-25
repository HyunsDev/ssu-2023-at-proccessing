# Subject: let's combine all of them


x = 100 #ball's x position
y = 100
xdir = 4 #ball’s direction
ydir = 4
diam = 50 #ball’s diameter
padX = 0
padY = 0
padWidth = 200
padHeight = 20

def setup():
    global padY, padHeight
    size(800, 600)
    padY = height - padHeight

def draw():
    global x, y, xdir, ydir, diam
    global padX, padY, padWidth, padHeight
    
    background(200)
    ellipse(x, y, diam, diam)
    x = x + xdir
    y += ydir # anther way to add
    
    if x + diam/2  > width:
        xdir = xdir * -1
        fill(255, 0, 0)
  
    if x - diam/2 < 0:
        xdir = xdir * -1
        fill(255, 255, 0)
        
    if y - diam/2 < 0:
        ydir = ydir * -1
  
    if y + diam/2 > height:
        ydir = ydir * -1

    padX = mouseX - padWidth/2
    fill(255)
    rect(padX, padY, padWidth, padHeight)

    # boucing with pad. need to know 'and' logical keyword
    if x > padX and x < padX + padWidth and y + diam/2 > padY:
        ydir = ydir * -1


# Homework: 
# - make it prettier
