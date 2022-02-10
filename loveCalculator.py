#   Create a program that will receive 2 names and will count the letter (t,r,u,e,l,o,v,e) in the names.
#   Program will then combine the countt number and result in percentage format as compatible percentage.

#   Name of Program: Love Calculator
#   Input: 2 Names (String Format)
#   Output: Love Score (Integer Format)
#   Process: Program will combine first name and second name, program count number of each letter (t,r,u,e,l,o,v,e), 
#            combines the total number to get percentage.


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your partner's name? \n") # Tambahan komen disini


name1_lower = name1.lower()
name2_lower = name2.lower()

name_combine = name1_lower+name2_lower

count1 = name_combine.count('t') + name_combine.count('r') + name_combine.count('u') + name_combine.count('e')
count2 = name_combine.count('l') + name_combine.count('o') + name_combine.count('v') + name_combine.count('e')

score_str = str(count1)+str(count2)
score_int = int(score_str)

if score_int > 40 and score_int < 50:
    print("Your score is {}%, you are alright together".format(score_int))
elif score_int < 10 or score_int > 90:
    print("Your score is {}%, you go like coke and mentos".format(score_int))
else:
    print("Your score is {}%".format(score_int))
