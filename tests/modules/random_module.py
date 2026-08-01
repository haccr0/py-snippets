import random

number = random.randint(1, 10)
choice = random.choice(["apple", "orange", "banana"])

guess = input("guess a no")

if int(guess) == number:
    print("you guessed it right")
else:
    print(f"you guessed it wrong the no was {number}")
