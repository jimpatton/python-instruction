print("Welcome to the Temperature Converter")
choice = "y"
while choice == "y".lower():
    f = float(input("\nEnter degrees in Fahrenheit: "))
    #c = (f-32) * 5/9
    c = (f-32) * 5/9
    print("Degrees in Celsius: " + str(c))
    choice = input("\nContinue? (y/n): ")
