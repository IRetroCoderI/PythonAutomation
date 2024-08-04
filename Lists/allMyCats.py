

catNames = []

while True:
    name = input(f'Enter the name of cat {len(catNames) + 1} (Or enter Nothing to stop):  ')
    
    if name == '':
        break
    
    catNames.append(name)

print('The cats names are: ')
for name in catNames:
    print('     ' + name)