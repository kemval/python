import getpass

class Player:
    
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.choice_value = ""

    def make_choice(self):
        while True:
            try:
                print(f"{self.name}, enter your choice (rock/paper/scissors):")
                self.choice_value = getpass.getpass(prompt="", stream=None)

                if self.choice_value.lower() not in ["rock", "paper", "scissors"]:

                    raise ValueError("Please choose 'rock', 'paper', or 'scissors'.")
                break

            except ValueError as e:
                print(e)

def winner(player1, player2):

    if player1.choice_value == player2.choice_value:
        return "It's a tie!"
    
    elif (player1.choice_value == "rock" and player2.choice_value == "scissors") or \
         (player1.choice_value == "paper" and player2.choice_value == "rock") or \
         (player1.choice_value == "scissors" and player2.choice_value == "paper"):
        
        player1.score += 1

        return f"{player1.name} wins!"
    
    else:
        player2.score += 1
        return f"{player2.name} wins!"

def main():
        
        player1_name = input("Enter player01 name: \n")
        player2_name = input("Enter player02 name: \n")

        player1 = Player(player1_name)
        player2 = Player(player2_name)

        while True:

            try:
                rounds = int(input("\nEnter number of rounds: "))
                break

            except ValueError:
                print("\nInvalid input. Please enter a valid number of rounds.")


        for round in range(rounds):

            player1.make_choice()
            player2.make_choice()

            print(f"{player1.name} chose {player1.choice_value}\n")
            print(f"{player2.name} chose {player2.choice_value}\n")

            result = winner(player1, player2)

            print(result)

        print("Final scores:")
        print(f"{player1.name}: {player1.score} wins")
        print(f"{player2.name}: {player2.score} wins")

while True:

    main()

    while True:
        try:
            question = input("\nWould you like to play again? (y or n)").title()
            if question == "N":
                exit()
            elif question == "Y":
                break
            else:
                raise ValueError("\nInvalid choice. Please choose 'y' or 'n'.")
            
        except ValueError as e:
            print(e)

