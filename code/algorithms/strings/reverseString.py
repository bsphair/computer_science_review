name = 'number'
length = len(name);
storage = ''

# option 1 (for loop)
for char in range(length - 1, -1, -1):
    storage += name[char]

# option 2 (while loop)
count = length - 1
while(count >= 0):
    storage += name[count]
    count -= 1

# option 3 (slice notation)
# Slice notation involves two colons and up to three values within the square brackets. [start:stop:step]
# By not included start and stop, the -1 tells to start at the end and go backwards
print(name[::-1])


print(storage)
