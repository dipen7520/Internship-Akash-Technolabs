number = []
for i in range(1, 3):
    number.append(int(input(f'Enter the number{i}: ')))

if number[0] == number[1]:
    print(f'{number[0]} and {number[1]} are equal.')
elif number[0] > number[1]:
    print(f'{number[0]} is greater than {number[1]}.')
else:
    print(f'{number[1]} is greater than {number[0]}.')