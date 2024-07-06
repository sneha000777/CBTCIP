import random
import prettytable

def get_user_choice():
    choice = input("Enter a choice (rock, paper, scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        if choice == "exit" or choice == "quit" or choice == "0":
            return 0
        elif choice == "score" or choice == "card" or choice == "stats" or choice == "results" or choice == "s":
            score_card(user_score, computer_score, games_played)
        elif choice == "clear" or choice == "cls":
            import os
            os.system("cls")
        elif choice == "help" or choice == "h" or choice == "info" or choice == "?":
            help_info()
        else:
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

def score_card(user_score, computer_score, games_played):
    global PT
    PT=prettytable.PrettyTable()
    PT.field_names = ["Score", "User", "Computer"]
    PT.add_row([games_played, user_score, computer_score])
    print(PT)
    if user_score > computer_score:
        print("Winning: User")
    elif user_score < computer_score:
        print("Winning: Computer")
    else:
        print("Winning: Tie")
    print()
    PT=prettytable.PrettyTable()

def help_info():
    print("\nEnter 'exit' at any time to quit the game.")
    print("Enter 'score' to view the current scores.")
    print("Enter 'clear' to clear the screen.\n")

def play_game():
    global user_score, computer_score, games_played
    PT=prettytable.PrettyTable()
    user_score = 0
    computer_score = 0
    games_played = 0
    print("<<========= Rock, Paper, Scissors =========>>\n")
    print("Welcome to Rock, Paper, Scissors!\n")
    help_info()
    while games_played < 20:
        user_choice = get_user_choice()
        if user_choice == 0:
            break
        computer_choice = get_computer_choice()
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.")
        
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
    else:
        print("Game over! You have played 20 games.\nTIME FOR A BREAK!!!\n\nThank you for playing tho!")
    
    print("Final Scores:")
    PT.field_names = ["Score", "User", "Computer"]
    PT.add_row([games_played, user_score, computer_score])
    print(PT)

    if user_score > computer_score:
        print(f"Congratulations! You won {user_score} games.")
    elif user_score < computer_score:
        print(f"Computer wins {computer_score} games. Better luck next time!")
    else:
        print(f"It's a tie of {user_score} games!")
    print("\nGame Stopped. Thank you for playing!")

play_game()
