import random

user_wins = 0
computer_wins = 0

rps = ["rock", "paper", "scissors"]

is_game_playing = True

while is_game_playing:
    user_input = input("\nType rock/raper/scissors or Q to Quit: ").lower()

    if user_input == "q":
        is_game_playing = False
        break
    
    if user_input not in rps :
        print("Please type a valid input\n")
        continue
    
    random_number = random.randint(0,2)
    user_number = rps.index(user_input)

    if user_number == random_number:
        print("\nComputer picked ", rps[random_number], "! It's a draw!!")
    elif user_number  == (random_number + 1) or user_number == (random_number - 2):
        print("\nComputer picked: ", rps[random_number], " -- You won!!\n")
        user_wins += 1
        continue
    else:
         print("\nComputer picked:", rps[random_number], " -- You lost!!\n")
         computer_wins += 1

print("""your wins : computer wins 
        %d : %d
      
        Goodbye!""" %(user_wins, computer_wins))
