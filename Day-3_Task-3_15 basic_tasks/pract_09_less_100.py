for i in range(3):
    number = int(input(f'Enetr the number: '))
    if number > 100:
        print(f'Number is greater than 100.')
    elif number == 100:
        print(f'Number is a 100.')
    else:
        if number % 2 == 0:
            print(f'Number is less than 100 and even.')
        else:
            print(f'Number is less than 100 and odd.')