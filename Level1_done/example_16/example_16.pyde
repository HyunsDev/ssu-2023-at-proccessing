# Subject: Time to make bricks up there
# - but it is a little hard
# - we will cover it after learning 'list' data type.
# - Here is just some introduction to 'collision detection'

# dist function
brick_alive = False

def setup():
    global brick_alive
    size(800, 600)
    brick_alive = True #boolean variable

def draw(): 
    global brick_alive
    
    background(200)
    fill(255, 255, 0) 
    ellipse(mouseX, mouseY, 100, 100)
    
    if brick_alive: 
        fill(255, 0, 0)
        ellipse(width/2, height/2, 100, 100)
  
    if brick_alive and dist(width/2, height/2, mouseX, mouseY) < 100: 
        brick_alive = False
    
  
