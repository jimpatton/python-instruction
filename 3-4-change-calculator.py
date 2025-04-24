print("Welcome to the Change Calculator")
choice = "y"
while choice == "y".lower():
    cents = int(input("\nEnter number of cents: "))
    quarters = int(cents / 25)
    cents = cents % 25
    dimes = int(cents / 10)
    cents = cents % 10
    nickels = int(cents / 5)
    cents = cents % 5
    pennies = cents
    print(f"\nQuarters: {quarters}")
    print(f"Dimes:\t  {dimes}")
    print(f"Nickels:  {nickels}")
    print(f"Pennies:  {pennies}")
    choice = input("\nContinue? (y/n) ")          
