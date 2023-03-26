# for loop with list

# without list
room0 = "dog"
room1 = "cat"
room2 = "bird"

print(room0)
print(room1)
print(room2)

# with list
rooms = ["dog", "cat", "bird"]

i = 0
while i < 3:
    print(rooms[i])
    i += 1

# list data type: we will cover this later

# for loop
for r in rooms:
    print(r)
