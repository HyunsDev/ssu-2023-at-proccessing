#bricks = [[True for x in range(10)] for y in range(10)]
bricks = [[True] * 10 for _ in range(10)]

def setup():
    size(500, 500)

def draw():
    background(0)

    fill(0xFFFF0000)
    for row_i, row in enumerate(bricks):
        for col_i, brick in enumerate(row):
            if brick: rect(col_i*50, row_i*50, 50, 50) 

def mousePressed():
    global bricks
    if bricks[mouseY//50][mouseX//50]:
        bricks[mouseY//50][mouseX//50] = False
    else:
        bricks[mouseY//50][mouseX//50] = True  





#
