import random

number = random.randint(1, 10)
attempts = 0

while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1
        if guess == number:
            print(f"Correct! Attempts taken: {attempts}")
            break
        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")
    except ValueError:
        print("Please enter a valid number!")