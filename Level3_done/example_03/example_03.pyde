# line drawing function

def setup():
    size(600, 600)

def draw():
    background(255)
    verticalLines()
    horizontalLines(20)

def verticalLines():
    strokeWeight(5)
    stroke(255, 0, 0)
    for x in range(0, width, 30):
        line(x, 0, x, 600)

def horizontalLines(thickness):
    strokeWeight(thickness)
    stroke(0, 0, 255)
    for y in range(0, height, 30):
        line(0, y, 600, y)
   
   
                            
# Mission
# - modify the functions: add more parameters



#






#
    
