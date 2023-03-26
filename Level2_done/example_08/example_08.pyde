# use dynamic mode

def setup():
    size(600, 600)
    frameRate(2)
    noStroke()

def draw():
    background(255)
  
    i = 0
    while i < 10:
        #fill(random(255))
        fill(random(255), random(255), random(255))
        #diam = random(200)    
        diam = random(100, 200)
        ellipse(random(width), random(height), diam, diam)
        i += 1
