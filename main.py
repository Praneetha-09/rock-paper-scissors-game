import random

user_score = 0
computer_score = 0

print("Welcome to Rock Paper Scissors Game")
print("Type rock, paper, or scissors")
print("Type quit to stop the game")

while True:

    user_choice = input("\nEnter your choice: ").lower()

    if user_choice == "quit":
        print("Game ended.")
        break

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Try again.")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a draw!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or
        (user_choice == "paper" and computer_choice == "rock")
        or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win this round!")
        user_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

    # Display scores
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

print("\nFinal Scores")
print("Your Score:", user_score)
print("Computer Score:", computer_score)

if user_score > computer_score:
    print("Congratulations! You won the game.")

elif computer_score > user_score:
    print("Computer won the game.")

else:
    print("The game ended in a draw.")