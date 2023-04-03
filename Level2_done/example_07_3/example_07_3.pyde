# text ouput on canvas and color variables

# text ouput on canvas
size(200, 200)
textSize(32)
text("score" + str(100), 10, 30)

# color variables and hexa-decimal numbers for color
c = color(255, 0, 0)
fill(c)
ellipse(100, 100, 100, 100)

c = 0x1100ff00
fill(c)
ellipse(150, 100, 100, 100)
