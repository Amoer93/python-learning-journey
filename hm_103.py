import random
print(random.randint(1, 3))
player_option = int(input("What would you like to choose? 1: scissors, 2: rock, 3: paper: "))
computer_option = random.randint(1, 3)
print(f"the player choose {player_option}")
print(f"the computer choose {computer_option}")
if player_option - computer_option == 1:
    print("You win!")
elif player_option - computer_option == 0:
    print("Tie")
else:
    print("You lose!")