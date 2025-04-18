print('Factorial Calculator')
choice = 'y'
while choice == 'y':
    nbr = int(input("Enter and integer that's greater than 0 and less than 10: "))
    factorial = 1
    for i in range(1,nbr+1):
        factorial*=i
    print(f'Factorial of {nbr} is {factorial}')
    choice = input('Continue? ')