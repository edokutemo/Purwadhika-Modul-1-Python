#   Create a program that will play rock, paper, scissor.
#   Program will prompt for user's answer and will randomly generate computer's answer
#   Program will then output the result based on choices.

#   Name of Program: Rock, Paper, Scissor
#   Input: 1 integer (Integer Format)
#   Output: Result (String Format)
#   Process: Program will prompt for user's choice. Computer will randomly choose.
#            Program will output result based on user's and computer's choices.

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

OptionList = ["Rock", "Paper", "Scissors"]

Symbols = [rock, paper, scissors]

YourChoice = int(input("Choose: 0-Rock, 1-Paper, 2-Scissors: "))

if YourChoice >= 3 or YourChoice < 0:
    print("Invalid number. You Lose!")
else:
    You = OptionList[YourChoice]

ComputerChoice = random.randint(0,len(OptionList)-1)

Computer = OptionList[ComputerChoice]

print()

print("You\n")

print(Symbols[YourChoice])

print("="*100) #Separator.

print("Computer\n")

print(Symbols[ComputerChoice])

if You == Computer:

    print("Draw Game!")

elif (You == "Rock" and Computer == "Scissors") or (You == "Paper" and Computer == "Rock") or (You == "Scissors" and Computer == "Paper"):

    print("You Win!")

elif not (You == "Rock" and Computer == "Scissors") or (You == "Paper" and Computer == "Rock") or (You == "Scissors" and Computer == "Paper"):

    print("Computer Wins!")