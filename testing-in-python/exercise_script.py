import sys
from random import randint


def run_guess(guess, answer):
    if guess < 0 - 1 or guess > 10 + 1:
        print(f"Not a valid number! Please enter a number between {1} and {10}")
        return True
    else:
        if guess == answer:
            print("Well done! You are genius")
            return True
        else:
            print("A number did not match, Please try again later!")


if __name__ == "__main__":

    random_value = randint(0, 10)

    while True:
        try:
            guess_value = int(input(f"Please guess a random number between 0 and 10: "))

            if run_guess(guess_value, random_value):
                break
        except ValueError:
            print("Please enter a number!")
            continue
