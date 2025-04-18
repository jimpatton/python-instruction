from contact import Contact
print("Welcome to the Contact List application")

choice = 'y'
while choice == 'y'.lower():
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    email = input('Enter email:  ')
    phone = input('enter phone: ')
    c = Contact(first_name=first_name, last_name=last_name, email=email, phone=phone)
    c.display_contact()

    choice = input('Continue (y/n)? ')

