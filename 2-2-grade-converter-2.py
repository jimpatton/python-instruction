print("Welcome to the Letter Grade Converter")

choice = 'y'
while choice == 'y'.lower():
    num_grade = int(input("Enter numerical grade: "))
    letter_grade = ""
    if num_grade >=88:
        letter_grade = "A"
    elif num_grade>=80:
        letter_grade = "B"
    elif num_grade >=68:
        letter_grade = "C"
    elif num_grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    
    print("Letter grade: " + letter_grade)
    choice = input("\nContinue? (y/n): ")


