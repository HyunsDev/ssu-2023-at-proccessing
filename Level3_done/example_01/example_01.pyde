# user-defined function
# - how to make and use you own functions

def setup():
    size(600, 600)
    
def draw():
    myEllipse()
    drawFace()

# function without paramters
def myEllipse():
    fill(255, 255, 0)
    ellipse(500, 500, 100, 100)

# drawing a face
def drawFace():
    # face
    fill(0xffffff00)
    stroke(0)
    strokeWeight(10)
    ellipse(100, 100, 200, 200)
    # eyes
    fill(0xff000000)
    ellipse(100-35, 100-20, 30, 30)
    ellipse(100+35, 100-20, 30, 30)
    fill(0xfffffffa)
    noStroke()
    ellipse(100-40, 100-25, 15, 15)
    ellipse(100+30, 100-25, 15, 15)
    # mouth
    noFill()
    stroke(0)
    arc(100, 100, 100, 100, 0+0.8, PI-0.8)
        
# What if you want to draw a face OTHER positions?
# - we will cover this later.
# - we need to use paramters for positions

# Mission
# - make your own function to draw anything





#
