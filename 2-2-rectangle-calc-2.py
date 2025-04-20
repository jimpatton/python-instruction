print("Welcome to the Rectangle Area and Perimeter Calculator")
choice = "y"
while choice == "y".lower():
    l = float(input("\nEnter length: "))
    w = float(input("Enter width: "))
    #area = l*w
    #perimeter = 2*(l+w)
    print("Area " + str(l*w))
    print ("Perimeter "+ str(2*(l+w)))
    choice = input("\nContinue? (y/n):")