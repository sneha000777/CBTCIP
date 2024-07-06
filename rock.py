import random

def get_user_choice():
    choice = input("Enter a choice (rock, paper, scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        choice = input("Enter a choice (rock, paper, scissors): ").lower()
    return choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    games_played = 0

    while games_played < 3:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
        
        result = determine_winner(user_choice, computer_choice)
        
        if result == "user":
            print("You win this round!\n")
            user_score += 1
        elif result == "computer":
            print("Computer wins this round!\n")
            computer_score += 1
        else:
            print("It's a tie!\n")
        
        games_played += 1

        print(f"Scores after game {games_played}:")
        print(f"User: {user_score}")
        print(f"Computer: {computer_score}\n")
    
    print("Final Scores:")
    print(f"User: {user_score}")
    print(f"Computer: {computer_score}")

    if user_score > computer_score:
        print("Congratulations! You won the best of 3 games.")
    elif user_score < computer_score:
        print("Computer wins the best of 3 games. Better luck next time!")
    else:
        print("It's a tie after 3 games!")

if __name__ == "__main__":
    play_game()
