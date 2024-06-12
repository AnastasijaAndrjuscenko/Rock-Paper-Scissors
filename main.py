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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

chosen = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if chosen == 0:
    print(rock)
elif chosen == 1:
    print(paper)
elif chosen == 2:
    print(scissors)

if 0 <= chosen <= 3:
    print("Computer chose:")
    com_chosen = random.randint(0, 2)
    if com_chosen == 0:
        print(rock)
    elif com_chosen == 1:
        print(paper)
    else:
        print(scissors)

    # Type 0 Rock, 1 for Paper or 2 for Scissors
    if com_chosen == 0 and chosen == 2:
        print("You lose")
    elif com_chosen == 2 and chosen == 1:
        print("You lose")
    elif com_chosen == 1 and chosen == 0:
        print("You lose")
    elif chosen == 0 and com_chosen == 2:
        print("You win!")
    elif chosen == 2 and com_chosen == 1:
        print("You win!")
    elif chosen == 1 and com_chosen == 0:
        print("You win!")
    elif chosen >= 3 or chosen < 0:
        print("You typed an invalid number, you lose!")
    else:
        print("It's a draw")
else:
    print("You typed an invalid number, you lose!")
