name = ''

while not name:
    name = input("Enter your name:")
print("How many guests will you have?")
numOfGuests = int(input()) #remember to cast int
if numOfGuests:
    print('be sure to have neough room for all your guests.')

print("done")