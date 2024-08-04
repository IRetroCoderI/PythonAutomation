import copy as c


catTitle = 'Zophie the Cat'

Name = catTitle[:6]

print(Name)

#References!

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print(cheese) 
print(spam)

eggs = c.deepcopy(spam) #creates brand new list, doesnt just copy reference