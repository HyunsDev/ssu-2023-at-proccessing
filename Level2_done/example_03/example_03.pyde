# Subject: summation with while statement 

# without using while loop
# This is non-sense
print("Sum from 1 to 10:")
print(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)

# let's use while loop
sum = 0
count = 1
while count <= 10:
    sum = sum + count
    count += 1

print("Sum from 1 to 10: ", sum)


# print even numbers
count = 1
while count <= 10:
    if count % 2 == 0:
        print(count, "is even number")
    count += 1
  
# Mission:
# - let's get the sum of 'even' numbers between 1 to 100
# - let's get the sum of 'odd' numbers between 1 to 100
# - let's get the sum of 'multiples of 3' between 1 to 100
