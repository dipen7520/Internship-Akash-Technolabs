for i in range(3):
    number = int(input(f'Enter the number: '))
    if number < 0:
        print(f'{number} is a negative.')
    elif number == 0:
        print(f'{number} is a zero.')
    else:
        print(f'{number} is a positive.')
