number = []
for i in range(1, 4):
    number.append(int(input(f'Enter the number{i}: ')))

if number[0] > number[1]:
    if number[1] > number[2]:
        print(f'{number[0]} is a greatest number.')
    else:
        print(f'{number[2]} is a greatest number.')
elif number[1] > number[0]:
    if number[1] > number[2]:
        print(f'{number[1]} is a greatest number.')
    else:
        print(f'{number[2]} is a greatest number.')