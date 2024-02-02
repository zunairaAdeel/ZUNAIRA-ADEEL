import random

num=random.randint(1,50)
guess=None
while guess!=num:
    guess=int(input('enter you guessing number between 1-10:'))
    guess=int(guess)
    if guess==num:
        print('congractulations you won!')
        break
    else:
        print("Try again!")
