animals = ["cat", "dog", "mouse", "elephant", "goldfish"]

print(animals[2])

#negative indexes move BACKWARDS

print(animals[-1])
print(animals[-2])

#you can add to the end of a list with negative index
animals[-1] = 'kittycat'
print(animals)
animalsCopy = animals
print(animalsCopy)
del animalsCopy[3:]
print(animalsCopy)
#slicing indexes x:y  start at x, end before y

print(animals[2:3])
print(animals[1:-1])

#you can leave out numbers on either side of the index

print(animals[:2])
print(animals[1:])


print(len(animals))