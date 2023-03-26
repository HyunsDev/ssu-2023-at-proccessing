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
        i += 1
    
# Mission
# - fill the canvas with circls in random position and random size
