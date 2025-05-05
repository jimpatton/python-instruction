def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error! Please enter a valid integer")

def main():    
    print("FizzBuzz Exercise")
    choice = "y"
    while (choice.lower() == "y"):
        nbr = get_valid_int("\nEnter number: ")    
        for i in range(1,nbr+1):
            if i % 15 == 0:
                print("fizzbuzz")
            elif i % 5 == 0:
                print("buzz")
            elif i % 3 == 0:
                print("fizz")
            else:
             print (i)
        choice = input("\nContinue? (y/n)")

if __name__ == "__main__":
    main()