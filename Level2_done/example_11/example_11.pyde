# color pallette

charts = [67, 89, 20, 10, 100, 90, 80, 50]
# color: alpha(opacity), red, green, blue
colors = [0xffff0000, 0xffffff00, 0xff0000ff, 0xff000000, 0xffffffff]
# https://py.processing.org/reference/color.html

import random 

def setup():
    size(600, 600)
    frameRate(1)

def draw():
    background(255)
    bar_height = height / len(charts)
  
    for i, c in enumerate(charts):
        fill(random.choice(colors))
        bar_width = c * width / 100
        rect(0, i * bar_height, bar_width, bar_height)
