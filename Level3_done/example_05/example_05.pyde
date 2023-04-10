# nested loop: loop inside another loop

# while loop
i = 0
while i < 5:
  print(i)
  i += 1
  
# nested while loop
i = 0
while i < 5:
    j = 0
    while j < 5:
        print("i:", i, "j:", j)
        j += 1
    i += 1

# for loop with range() function    
for i in range(5):
    print(i)

# string formating
print("I am %i years old" % 10)
print("I am %i years old and %f cm tall" % (10, 172.1))
print("I am %i years old and i love %s" % (10, "running"))

#multiplication table using for loop
for i in range(1, 5):
    print("%i * %i = %i" % (1, i, 1*i))
    
# nested for loop
for i in range(1, 5):
    for j in range(1, 5):
        print("%i * %i = %i" % (i, j, i*j))
        #print(f"{i} * {j} = {i*j}") # f-string
        
        

#
