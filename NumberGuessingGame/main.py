import random

highest_num = 100
lowest_num = 1
guesses = 0
is_running = True
number = random.randint(lowest_num, highest_num)

print("***PYTHON NUMBER GUESSING GAME***")
print(f"Enter a number between {lowest_num} and {highest_num}")
while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("Guess is out of range")
            print("Please enter a guess between 1 and 100")


        elif guess > number:
            print("Too high! Try again")

        elif guess < number:
            print("Too low! Try again")

        else:
            print(f"Correct! The number was {number}")
            print(f"Total number of guesses: {guesses}")
            is_running = False

    else:
        print("Invalid guess")
        print("Please enter a guess between 1 and 100")


