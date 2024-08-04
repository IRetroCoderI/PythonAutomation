spam = ['apples', 'bananas', 'tofu', 'cats']
numbers = ['one', 1, 'two', 'three', 'four']

#write a function that takes a list value as an argument and returns a string with all the items seperated byh a comma and a space, with and inserted before the last item

def addComma(words):
    sentence = ''
    for word in words:
        if word != words[-1]:
            sentence += str(word) + ", "
        else :
            sentence += "and " + str(word)
            break
    
    print(sentence)

addComma(spam)
addComma(numbers)
addComma([])