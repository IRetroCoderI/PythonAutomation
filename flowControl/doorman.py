import password

key = password.key

phrase = ''
count = 1
while phrase != 'q':
    phrase = input(f"What is the password? {count} Attemps. ")
    if phrase: #if phrase exists, or if phrase is not empty ('')
        if phrase == key:
            print("Password Accepted!")
            count+=1
            exit()
        else:
            print("DENIED")
            count+=1
    else: #if phrase is empty...
        print("You did not enter a phrase, BEGONE")
        count+=1