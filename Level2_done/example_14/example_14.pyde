# ball
x = 0
y = 0
diam = 30
xdir = 6
ydir = 6
ballColor = 0xffffff00

# pad
padX = 0
padY = 0
padWidth = 200
padColor = 0xff00ff00

# bricks
bColNo = 10
bWidth = 0
bHeight = 0
bricks = [True for i in range(bColNo)]
# bricks = [True] * 10

def setup():
    size(800, 600)
    global x, y, diam, xdir, ydir, ballColor
    global padX, padY, padWidth, padColor
    global bColNo, bWidth, bHeight
  
    x = width / 2
    y = height / 2
    diam = 30
    xdir = 6
    ydir = 6
    ballColor = 0xffffff00

    padX = width/2
    padY = height-20
    padWidth = 200
    padColor = 0xff00ff00
  
    bColNo = 10
    bWidth = width / bColNo
    bHeight = 30
  

def draw():
    background(200)
    global x, y, diam, xdir, ydir, ballColor
    global padX, padY, padWidth, padColor
    global bColNo, bWidth, bHeight
    
    # drawing a ball
    fill(ballColor)
    ellipse(x, y, diam, diam) 
    x += xdir
    y += ydir 
    
    # drawing racket...
    fill(padColor)
    padX = mouseX - padWidth/2
    rect(padX, padY, padWidth, 20, 15)
    
    for i, brick in enumerate(bricks):
        if brick:
            fill(0xff7E8AF0)
            rect(i*bWidth, 0, bWidth, bHeight, 50)        
    
    # ball bouncing 
    if x - diam/2 < 0: # left side check
        xdir *= -1
        #padWidth = padWidth - 10
    
    if x + diam/2 > width: # right side check
        xdir *= -1
        #padWidth = padWidth - 20
    
    if y - diam/2 < 0:
        ydir *= -1
    
    if y + diam/2 > height:
        ydir *= -1
    
    # checking collision with a pad
    if x > padX and x < padX + padWidth and y > padY-diam/2:
        ydir *= -1
        fill(0xffFF0000)
        rect(padX+2, padY+2, padWidth-4, 16, 15)
    
    # if the ball in in the region of bricks
    if y < bHeight:
        # when the ball hits the bricks
        if bricks[x / bWidth]:
            ydir *= -1
            bricks[x / bWidth] = 0 
        
        



  
    
#  
        
