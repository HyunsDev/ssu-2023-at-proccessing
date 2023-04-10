# mouse interactions

def setup():
    size(600, 600)
    noStroke()
  
def draw():
    background(0)
    for x in range(0, width, 30):
        for y in range(0, height, 30):
            r = dist(mouseX, mouseY, x, y) / 20
            ellipse(x+15, y+15, r, r)
  
