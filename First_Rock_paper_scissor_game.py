import random
choices = ["rock","paper","scissor"]
computer_choice = random.choice(choices)
start_game = input("to start game enter start to not engage enter exit : ")
start_game.lower()
if start_game == "start":
    
    player_choice = input("enter the choice ( rock , paper , scissor) or enter exit for exiting game : ")
    player_choice.lower()
    while player_choice != "exit" : 
        if player_choice == computer_choice :
            print("draw both choices are equal ")
        elif player_choice == "rock" and computer_choice == "paper" :
            print("you lose computer choose paper")
        elif player_choice == "rock" and computer_choice == "scissor" :
            print("you win computer choose scissor")
        elif player_choice == "paper" and computer_choice == "rock" :
            print("you win computer choose rock")
        elif player_choice == "paper" and computer_choice == "scissor" :
            print("you lose computer choose scissor")
        elif player_choice == "scissor" and computer_choice == "paper" :
            print("you win computer choose paper")
        elif player_choice == "scissor" and computer_choice == "rock" :
            print("you lose computer choose rock")
        player_choice = input("enter the choice ( rock , paper , scissor) or enter exit for exiting game : ")
    print("thanks for enjoying 💀")
