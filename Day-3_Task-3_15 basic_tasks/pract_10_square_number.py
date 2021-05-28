for i in range(3):
    number = int(input(f'Enter the number: '))
    if number > 10:
        print(f'Number is not less than 10.')
    elif number == 10:
        print(f'Number is a 10.')
    else:
        print(f'Square of {number} is a {number*number}')