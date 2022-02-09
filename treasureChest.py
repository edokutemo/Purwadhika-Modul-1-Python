print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

answer = input('''You're at a cross road. Where do you go? Type "Left" or "Right" \n''')

while answer != "Exit":
    if answer == "Right":
        print("You fall into a hole. Game Over")
    elif answer == "Left":
        answer = input(
            '''You come to a lake. There is an island in the middle of the lake. Type "Wait" to wait for boat. Type "Swim" to swim across\n''')
        if answer == "Swim":
            print("You have been attacked by trouts. Game Over")
            break
        elif answer == "Wait":
            answer = input(
                '''You've arrived at the island unharmed. There is a house with 3 doors. "Red", "Yellow", and "Blue". Which colour you choose?\n''')
            if answer == "Red":
                print("You've been burned by fire. Game Over")
                break
            elif answer == "Blue":
                print("You've been eaten by beast. Game Over")
                break
            elif answer == "Yellow":
                print("You've won!")
                break
            else:
                print("Game Over")
                break
    break
