print("Greatest Common Divisor Finder")
choice = "y"
while choice.lower() == "y":
    x = int(input("\nEnter first number: "))
    y = int(input("Enter second number: "))
    if (x>y):
        temp =x
        x = y
        y = temp
    while (y != 0):
        remainder = x % y
        x = y
        y = remainder
    print (f"Greatest common divisor: {x}")
    choice = input("\nContinue? (y/n):")
