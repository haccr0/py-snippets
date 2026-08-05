import random

print("guess the number game, you have 10 guesses")

msg = "But you're very close"
msg_2 = "you're very very very close"


def function():

    guess_no = random.randint(1, 100)
    attempts = 10

    while attempts > 0:
        user_guess = input("Guess a number between 1 and 100: ")

        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_guess < 1 or user_guess > 100:
            print("Please guess a number between 1 and 100.")
            continue

        attempts -= 1

        if (
            user_guess < guess_no + 3
            and user_guess > guess_no - 3
            and user_guess != guess_no
        ):
            if user_guess < guess_no:
                print(f"Too low! {msg_2}. Try again.")
            else:
                print(f"Too high! {msg_2}. Try again.")

        elif (
            user_guess < guess_no + 6
            and user_guess > guess_no - 6
            and user_guess != guess_no
        ):
            if user_guess < guess_no:
                print(f"Too low! {msg}. Try again.")
            else:
                print(f"Too high! {msg}. Try again.")
        elif user_guess < guess_no:
            print("Too low! Try again.")
        elif user_guess > guess_no:
            print("Too high! Try again.")
        else:
            print(
                f"Congratulations! You guessed the number {guess_no} in {10 - attempts} attempts."
            )
            break
        print(f"You have {attempts} attempts left.")
    else:
        print(f"Sorry, you've used all your attempts. The number was {guess_no}.")


while True:
    function()

    try_again = input("want to try again?: Y/N").strip().upper()

    if try_again in ("YES", "Y"):
        continue
    elif try_again in ("NO", "N"):
        print("thank you!")
        break
    else:
        print("thank you!")
        break
