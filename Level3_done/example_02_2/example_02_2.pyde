# loop statement: for loop(review)
# pl. refer this page: 
# https://wikidocs.net/22

# basics for loop: range() function
for x in range(5):
    print(x)

for x in range(0, 5):
    print(x)

for x in range(0, 5, 1):
    print(x)

for x in range(0, 5, 2):
    print(x)    

for x in range(2, 10, 2):
    print(x)
    
for x in range(10, 0, -2):
    print(x)
             
# for loop having if statement
for x in range(5):
  if x % 2 == 0:
    print(x)

# for loop with string
for c in "Python":
  print(c)

# for loop with list
for e in [1, 2, 10, 100]:
  print(e)

scores = [10, 20, 10, 100, 1000]
for e in scores:
    print(e)
    
for i, e in enumerate(scores):
    print(i, e)    
    
 
    
          
#
