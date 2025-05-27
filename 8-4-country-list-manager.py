items = []

def display_menu():
    print("\nCOMMAND MENU")
    print("1 - List countries")
    print("2 - Add a country")
    print("3 - Exit\n")

def list_countries():
    if not items:
        print ("No countries in list\n1")
    else:
        items.sort()
        for country in items:
            print(country)

def add_country():
    country = input("\nEnter country: ")
    items.append(country)
    print(f"{country} has been added. \n")

def main():
    command = ""
    while command != "3":
        print("\nCountry List Manager")
        display_menu()
        command = input("Enter menu number: ")
        if command == "1":
            list_countries()
        elif command == "2":
            add_country()
        elif command == "3":
            exit
        else:
            print("Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
