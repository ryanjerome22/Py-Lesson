import random 

def get_choices ():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice (options)

    choices = {"player" : player_choice, "computer" : computer_choice}
    return choices

def check_win (player, computer):
    print (f"You chose player {player} , computer chose {computer} " )
    if player == computer:
        return "Its a tie!"
    
    elif player == "rock" :
        if computer == "scissors":
            return "Rock smashes scissors! You Win! "
        else: 
            return "Paper covers rock! You Lose. "
    
    elif player == "paper" :
        if computer == "rock":
            return "Paper covers rock! You Win! "
        else:
            return "Scissors cuts paper! You Lose. "

    elif player == "scissors" :
        if computer == "paper":
            return "Scissors cuts paper! You Win! "
        else:
            return "Scissors can't cut rock! You Lose. "

choices= get_choices()
result= check_win(choices["player"], choices["computer"])

print (result)