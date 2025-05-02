print("Welcome to the Factorial Calculator")
choice = "y"
while choice == "y".lower():
    nbr = int(input("\nEnter and integer that's greater than 0 and less than 10: "))
    factorial = 1
    for i in range(1,nbr+1):
        factorial *=i
    print(f"The factorial of {nbr} is {factorial}")
    choice = input("\nContinue? (y/n): ")