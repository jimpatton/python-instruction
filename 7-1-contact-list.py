from contact import Contact
import re
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern,email) is not None

def is_valid_phone(phone):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return re.match(pattern,phone) is not None

def main():
    print("Welcome to the Contact List application")
    choice = 'y'
    while choice == 'y'.lower():
        first_name = input('\nEnter first name: ')
        last_name = input('Enter last name: ')
        email = input('Enter email:  ')
        while not is_valid_email(email):
            print("Please enter a valid email address")
            email = input("Enter email: ")
        phone = input('Enter phone: ')
        while not is_valid_phone(phone):
            print("Please enter phone in format xxx-xxx-xxxx")
            phone = input("Enter phone: ")
        c = Contact(first_name=first_name, last_name=last_name, email=email, phone=phone)
        c.display_contact()

        choice = input('Continue (y/n)? ')

if __name__ == "__main__":
    main()