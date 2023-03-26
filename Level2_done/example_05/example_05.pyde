# drawing rectangles with while loop
size(500, 500)

fill(128)
x = 0
while x < width: # Processing variable
    fill(x / 2) # tip for color selection based on x coordinates
    rect(x, 0, 100, 100)
    x += 100

# drawing circles with while loop
x = 50 

while x < width:
    fill(255 - x / 2) # tip for color selection based on x coordinates
    ellipse(x, 200, 100, 100)
    x += 100
  
# Mission
# - use REAL color to fill the shapes
# - fill the canvas with rectangles in different colors
