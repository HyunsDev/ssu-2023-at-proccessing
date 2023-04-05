# color pallette
# color: alpha(opacity), red, green, blue
colors = [0xffff0000, 0xffffff00, 0xff0000ff, 0xff000000, 0xffffffff]
#colors[10]
# https://py.processing.org/reference/color.html

import random 

def setup():
    size(600, 600)
    frameRate(1)

def draw():
    background(255)
 
    i = 0
    while i < 10:
        fill(random.choice(colors))
        diam = random.random() * 200
        ellipse(random.random()*width, random.random()*height, diam, diam)
        i += 1
        
        
        
        
        
        
        

#
