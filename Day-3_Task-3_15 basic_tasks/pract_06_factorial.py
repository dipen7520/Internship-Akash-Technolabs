number = int(input(f'Enetr the number: '))
fact = 1

if number < 0:
    print(f"Factorial doesn't exists fro negative number.")
elif number == 0:
    print(f'Factorial of 0 is 1.')
else:
    for i in range(1, number+1):
        fact = fact * i
    print(f'Factorial of {number} is a {fact}.')
