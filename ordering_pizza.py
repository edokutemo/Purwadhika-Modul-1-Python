#   Create a program that will prompt the Size (S, M, L), Pepperoni (Y, N), and Cheese (Y, N).
#   Program needs to sum all the price and outtput the total price.

#   Name of Program: Pizza Order
#   Input: 3 Letters (String Format)
#   Output: Total Bill (Integer Format)
#   Process: Program will prompt 3 questions (size, pepperoni topping, extra cheese). 
#            Program will sum the price and return the total bill


print("Welcome to Python Pizza Deliveries!")

# Prompt for inputt, In this case is case sensitive (MUST BE UPPER CASE)
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# Variable bill is to store sum of prices. Starts from 0.
bill = 0

# If statement according to each variables and the input entered.
# Will then adds the price to variable bill.
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1

print("Your total bill is :${}".format(bill))

