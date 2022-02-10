numbers = []
numbers_int = []

for i in range(1, 101):
    numbers.append(str(i))

for i in range(1, 101):
    numbers_int.append(i)

for i in range(len(numbers)):
    number = numbers[i-1]
    number_integer = numbers_int[i-1]
    if '7' in number:
        print("up")
    elif number_integer % 7 == 0:
        print("up")
    else:
        print(i)