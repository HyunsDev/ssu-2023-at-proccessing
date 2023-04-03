def setup():
    size(600, 600)
    stroke(0, 0, 255)
    strokeWeight(3)

def draw():
    i = 0
    while i < 100:
        x = random(width)
        y = random(height)
        point(x, y)
        #point(random(width), random(height))
        i += 1
    
# Mission
# - fill the canvas with circls in random position, random color, and random size



#
