number = []
for i in range(1, 3):
    number.append(int(input(f'Enter the number{i}: ')))

number[0], number[1] = number[1], number[0]

print(f'number1 is {number[0]}')
print(f'number2 is {number[1]}')