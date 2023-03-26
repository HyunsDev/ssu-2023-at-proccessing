bricks = [[True for x in range(10)] for y in range(10)]

def setup():
    size(500, 500)

def draw():
    background(0)

    for x, r in enumerate(bricks):
        for y, b in enumerate(r):
            if b:
                fill(0xFFFF0000)
            else:
                fill(0)

            rect(x*50, y*50, 50, 50) 

def mousePressed():
    if bricks[mouseX/50][mouseY/50]:
        bricks[mouseX/50][mouseY/50] = False
    else:
        bricks[mouseX/50][mouseY/50] = True  
  
