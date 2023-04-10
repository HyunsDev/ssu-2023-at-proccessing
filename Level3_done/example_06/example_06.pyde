# drawing something with nested for loop

def setup():
    size(600, 600)
    frameRate(2)

def draw():
    s = 100
    for x in range(0, width, s):
        for y in range(0, height, s):
            fill(random(255))
            rect(x, y, s, s)
            fill(random(255))
            ellipse(x+50, y+50, s, s)
    
