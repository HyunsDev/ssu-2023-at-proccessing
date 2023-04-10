# user-defined function "with parameters"
# - with parameters, you can give some other different actions
# - to the function.

def setup():
    size(600, 600)
    myEllipse2(0xffff0000)
    drawFace2(100, 100)
    drawFace2(100, 300)
    drawFace3(100, 500, 0xff00ff00)

def draw():
    pass # when you want to leave the draw() function empty

def myEllipse2(c):
    fill(c)
    ellipse(500, 500, 100, 100)

# drawing a face at some posotions
def drawFace2(x, y):
    # face
    fill(0xffffff00)
    stroke(0)
    strokeWeight(10)
    ellipse(x, y, 200, 200)
    # eyes
    fill(0xff000000)
    ellipse(x-35, y-20, 30, 30)
    ellipse(x+35, y-20, 30, 30)
    fill(0xfffffffa)
    noStroke()
    ellipse(x-40, y-25, 15, 15)
    ellipse(x+30, y-25, 15, 15)  
    # mouth
    noFill()
    stroke(0)
    arc(x, y, 100, 100, 0+0.8, PI-0.8)

def mousePressed():
    drawFace2(mouseX, mouseY)
        
            
# drawing a face
def drawFace3(x, y, c):
    # face
    fill(c) #
    stroke(0)
    strokeWeight(10)
    ellipse(x, y, 200, 200)
    # eyes
    fill(0xff000000)
    ellipse(x-35, y-20, 30, 30)
    ellipse(x+35, y-20, 30, 30)
    fill(0xfffffffa)
    noStroke()
    ellipse(x-40, y-25, 15, 15)
    ellipse(x+30, y-25, 15, 15)  
    # mouth
    noFill()
    stroke(0)
    arc(x, y, 100, 100, 0+0.8, PI-0.8)
    
    
# Mission
# - modify these functions:
# - add more paramters such as eye size and mouse size et al





#
