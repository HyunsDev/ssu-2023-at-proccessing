# random line drawing function

def setup():
    size(600, 600)

def draw():
    background(255)
    randomLinesFrom(mouseX, mouseY)

def randomLinesFrom(cx, cy):
    for lines in range(10):
        strokeWeight(random(10))
        stroke(random(255))
        line(cx, cy, random(width), random(height))
        
# Mission
# - modify the functions: add more parameters






#
            
