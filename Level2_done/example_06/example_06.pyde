size(600, 600)

# random function test
print(random(100))
print(random(100, 200))

# random number generation using while
i = 0
while i < 5:
    print(random(100), random(100, 200))
    i += 1 #i = i + 1
  
  
# random size of shapes
i = 0
while i < 5:
    ellipse(random(width), random(height), random(100), random(100))
    i += 1

# another way
fill(255, 0, 0)    
i = 0
while i < 5:
    s = random(100)
    ellipse(random(width), random(height), s, s)
    i += 1
