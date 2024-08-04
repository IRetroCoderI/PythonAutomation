import random

eightBall = ['It is certain',
             'It is decidedly so',
             'Yes definitely',
             'Reply hazy try again',
             'Ask again later',
             'Concentrate and ask again',
             'My reply is no']

while True:
    user = input("I am the magic 8-Ball! Ask me anything!: ")
    if user == '':
        break

    print(random.choice(eightBall))