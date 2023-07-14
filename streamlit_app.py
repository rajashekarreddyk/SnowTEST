
import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < secret_number:
            print("Too low. Try again!")
        elif guess > secret_number:
            print("Too high. Try again!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == '__main__':
    guess_number()

import snowflake.connector
