import random

options = ("rock", "paper", "scissors")
running = True
score = 0
counter = 0

print("*PYTHON ROCK PAPER SCISSORS GAME*")
while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice(rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
        score += 1
    elif player == "scissors" and computer == "paper":
        print("You win!")
        score += 1
    elif player == "paper" and computer == "rock":
        print("You win!")
        score += 1
    else:
        print("You lose!")

    counter += 1

    if not input("Do you wish to play again?(y/n): ").lower() == "y":
        print("THANKS FOR PLAYING!")
        print(f"Your score is: {score}/{counter}")
        break
    