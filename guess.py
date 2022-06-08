#Guess the Number Game
import random

print("******************************")
print("****   Guess the number   ****")
print("******************************\n")

secret_number = random.randrange(1, 101)
attempts = 0

print("Guess the number, it's between 1-100. GO!")
print('What difficulty do you wanto to play?')
print('(1)-Easy\n(2)-Medium\n(3)-Hard')
level = int(input('Choose one:'))

if (level == 1):
    attempts = 20
elif (level == 2):
    attempts = 10
elif (level == 3):
    attempts = 5

for round in range(1, attempts + 1):
    print('bid number {} of the {} round'.format(round, attempts))
    bid = int(input('Guess a number: '))

    done = bid == secret_number
    bigger = bid > secret_number
    smaller = bid < secret_number

    if (bid < 1 or bid > 100):
        print('Please, choose a number between 1-100')
        continue
    if (done):
        print('Nice! You got it!')
        break
    else:
        if (bigger):
            print('WRONG! The number is smaller than that...')
        elif (smaller):
            print('WRONG! The number is bigger than that...')
print('Game over')
