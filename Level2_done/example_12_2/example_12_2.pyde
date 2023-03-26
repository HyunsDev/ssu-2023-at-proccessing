# making bricks

bricks = [True for x in range(10)]
      
def setup():
    size(500, 500)


def draw():
    background(0)

    for x, b in enumerate(bricks):
        if b:
            fill(0xFFFF0000)
        else:
            fill(0)

        rect(x*50, 0, 50, 50) 


def mousePressed():
    if mouseY < 50:
        if bricks[mouseX/50]:
            bricks[mouseX/50] = False
        else:
            bricks[mouseX/50] = True  
  
