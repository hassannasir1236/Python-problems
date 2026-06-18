import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves_lists = [rock, paper, scissor]
moves_names_lists = ["Rock", "Paper", "Scissor"]
user_input = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor. "))
print("User select move ", moves_names_lists[user_input], ":" , moves_lists[user_input])


computerMoves = random.randint(0, 2)
print("Computer select move ", moves_names_lists[computerMoves], ":" , moves_lists[computerMoves])

if user_input == computerMoves:
    print("Match Tie!")
elif (user_input == 0 and computerMoves == 2) or \
     (user_input == 1 and computerMoves == 0) or \
     (user_input == 2 and computerMoves == 1):
    print("You Win!")
else:
    print("You Lose!")

