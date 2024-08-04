spam = ['hello', 'world', 'how', 'howdy', 'there', 'ago']

print(spam.index('howdy')) #retrieves index of element

animals = ['cat', 'dog', 'mouse', 'elephant']
animals.append('moose')
print(animals)
animals.insert(0, 'chicken')
print(animals)
animals.remove('dog')
print(animals)

animals.append('axolotl')
animals.append('bear')
print(f"befores sorting:\n\t{animals}")
animals.sort()
print(f"after sorting:\n\t{animals}")

