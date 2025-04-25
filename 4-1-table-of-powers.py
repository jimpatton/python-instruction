print("Welcome to the Squares and Cubes table")
choice = "y"
while choice == "y".lower():
    nbr = int(input("\nEnter an integer: "))
    print("\nNumber\tSquare\tCube")
    print("======\t======\t=====")
    for i in range(1, nbr + 1):
        print(f"{i}\t{i**2}\t{i**3}")
    choice = input("\nContinue? (y/n) ")
    