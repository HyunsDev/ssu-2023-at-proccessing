#  opacity <--> transparency

size(600, 600)

fill(255, 0, 0)
ellipse(300, 300, 300, 300)

fill(255, 255, 0, 50) # the last parameter is opacity: 0 means totally transparent.
ellipse(150, 300, 300, 300)

fill(0, 0, 255, 255) # the last parameter is opacity
ellipse(450, 300, 300, 300)

fill(128, 128) # the last parameter is opacity
ellipse(300, 450, 300, 300)
