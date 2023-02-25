# Subject: Programming modes
# - static programming mode
# - dynamic programming mode

# In dynamic programming mode, 
# you need to fill in setup() and draw() funcitons.

# variables
i = 0

def setup():
    size(400, 400)
    global i # which means that in this setup() function,  i means global variable
    i = 1
    print("This is setup function:", i)


def draw():
    global i
    print("This is the draw function:", i)
    i = i + 1
