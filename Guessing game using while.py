import random

n=20
to_be_guessed=int(n*random.random())+1
guess=0

while guess != to_be_guessed:
    guess=int(input("new number:"))
    if guess > 0:
        if guess<to_be_guessed:
            print("Number is too small")
        elif guess>to_be_guessed:
            print('Number is too large')
    else:
        print('Sorry you are giving up')
        break
else:
    print('Congratulations you are made it')
