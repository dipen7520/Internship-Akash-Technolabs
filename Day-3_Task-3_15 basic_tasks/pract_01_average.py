sum = 0.0
avg = 0.0
for i in range(1,6):
    sum = sum + float(input(f'Enter the number{i}: '))

avg = sum / 5
print(f'The average is {avg}.')