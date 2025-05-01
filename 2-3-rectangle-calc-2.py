def get_positive_float(prompt):
    while True:
        value = input(prompt)
        try:
            num = float(value)
            if num >0:
                return num
            else:
                print("Error! Enter a positive number")
        except ValueError:
            print("Error! Please enter a numeric value.")

def main(): 
    print("Welcome to the Rectangle Area and Perimeter Calculator")
    choice = "y"
    while choice.lower() == "y":
        l = get_positive_float("\nEnter length: ")
        w = get_positive_float("Enter width: ")
        area = l*w
        perimeter = 2*(l+w)
        print(f"Area: {area:.2f}")
        print(f"Perimeter: {perimeter:.2f}")
        choice = input("\nContinue? (y/n):")

if __name__ == "__main__":
    main()