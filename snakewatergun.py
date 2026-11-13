import random

def game_win(computer, player):
    # If both choices are the same, it's a tie
    if computer == player:
        return None

    # Check all possibilities when computer chooses 's' (Snake)
    if computer == 's':
        if player == 'w':
            return False  # Snake drinks water -> Computer wins
        elif player == 'g':
            return True   # Gun kills snake -> Player wins

    # Check all possibilities when computer chooses 'w' (Water)
    elif computer == 'w':
        if player == 'g':
            return False  # Gun drowns in water -> Computer wins
        elif player == 's':
            return True   # Snake drinks water -> Player wins

    # Check all possibilities when computer chooses 'g' (Gun)
    elif computer == 'g':
        if player == 's':
            return False  # Gun kills snake -> Computer wins
        elif player == 'w':
            return True   # Gun drowns in water -> Player wins


# List of choices for the computer
choices = ['s', 'w', 'g']
computer_choice = random.choice(choices)

# Get player's choice
player_input = input("Enter your choice: Snake (s), Water (w), or Gun (g): ").lower()

# Validate input
if player_input not in choices:
    print("Invalid choice! Please choose 's', 'w', or 'g'.")
else:
    result = game_win(computer_choice, player_input)

    print(f"\nComputer chose: {computer_choice} ('s' = Snake, 'w' = Water, 'g' = Gun)")
    print(f"You chose:      {player_input}\n")

    if result is None:
        print("It's a tie!")
    elif result:
        print("Congratulations! You win!")
    else:
        print("You lose! Computer wins!")
