print("Welcome to Guess the Number!")
import random

def generate_number():
    return random.randint(1, 10)

print("Welcome to Guess the Number!")
import random

def generate_number():
    return random.randint(1, 10)

def check_guess(secret, guess):
    return secret == guess

print("Welcome to Guess the Number!")
import random

def generate_number():
    return random.randint(1, 10)

def check_guess(secret, guess):
    return secret == guess

secret = generate_number()
guess = int(input("Guess a number from 1 to 10: "))

if check_guess(secret, guess):
    print("You win!")
else:
    print(f"You lose! The number was {secret}")

import random

def generate_number():
    return random.randint(1, 10)

def check_guess(secret, guess):
    return secret == guess

def play_game():
    secret = generate_number()
    guess = int(input("Guess a number from 1 to 10: "))

    if check_guess(secret, guess):
        print("You win!")
    else:
        print(f"You lose! The number was {secret}")

if __name__ == "__main__":
    print("Welcome to Guess the Number!")
    play_game()
