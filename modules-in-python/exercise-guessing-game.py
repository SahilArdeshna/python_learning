import sys
from random import randint

start = int(sys.argv[1]) or 0
end = int(sys.argv[2]) or 10

random_value = randint(start, end)

while True:
    try:
        guess_value = int(input(f'Please guess a random number between {start} and {end}: '))

        if guess_value < start - 1 or guess_value > end + 1:
            print(f'Not a valid number! Please enter a number between {start} and {end}')
            break
        else:
            if guess_value == random_value:
                print('Well done! You are genius')
                break
            else:
                print('A number did not match, Please try again later!')
    except ValueError:
        print('Please enter a number!')
        continue


