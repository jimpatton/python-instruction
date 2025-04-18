from dataclasses import dataclass

@dataclass
class Contact:
    first_name:str
    last_name:str
    email:str
    phone:str

    def display_contact(self):
        display_str ="---------------------------------------------\n"
        display_str +="----Current Contact---------------------------\n"
        display_str +="----------------------------------------------\n"
        display_str +=(f'Name:\t\t {self.first_name} {self.last_name}\n') 
        display_str +=(f'Email Address:\t {self.email}\n')
        display_str +=(f'Phone Number:\t {self.phone}\n')
        display_str +="---------------------------------------------"
        print(display_str)



