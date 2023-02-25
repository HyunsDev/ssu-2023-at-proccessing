# Subject: setting stroke colors and draw other shapes
# https://processing.org/reference

# Pl. remember this.
# fill() changes filling colors
# stroke() changes stroke colors

# let's draw different kinds of shapes
size(600, 600)

# stroke()
stroke(255) # 255 is white, 0 is black
ellipse(100, 100, 200, 200)

# noStroke(): after this function call, it doesn't draw stroke lines
noStroke()
fill(0, 255, 0)
ellipse(300, 100, 200, 200)

stroke(0)
fill(255, 0, 0)
ellipse(500, 100, 200, 200)

stroke(255, 0, 0)
ellipse(400, 4400, 100, 100)

# strokeWeight(): change stroke width
strokeWeight(10)
ellipse(100, 300, 200, 200)

strokeWeight(1)
# line()
line(0, 0, 600, 600)

# rect()
fill(0, 0, 255)
rect(200, 300, 300, 200)

# trangle()
fill(255, 255, 0)
triangle(100, 550, 300, 400, 400, 500)

# Practice: 
# use more than 5 colors and more than 5 shapes
