# Subject: draw and move the pad

padX = 0
padY = 0
padWidth = 200
padHeight = 20

def setup():
    global padY, padHeight
    size(800, 600)
    padY = height - padHeight

def draw():
    global padX, padY, padWidth, padHeight
    background(200)
    padX = mouseX - padWidth/2
    rect(padX, padY, padWidth, padHeight)
