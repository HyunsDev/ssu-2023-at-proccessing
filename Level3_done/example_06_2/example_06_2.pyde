# list of list
# pl. refer this page
# https://pythonexamples.org/python-list-of-lists/

samples = [['a', 25, 69, 'Apple'],
           [5, 'doll', 854, 41.2],
           [8, 6, 'car', True]]

print(samples)
print(samples[0])
print(samples[1])
print(samples[2])
#print(samples[3])

print(samples[0][0])
print(samples[2][2])


# for loop for list
for row in samples:
    print(row)


# nested loop for list of list
for row in samples:
    for e in row:
        print(e)



#
