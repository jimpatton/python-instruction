from grade import Grade

print("Letter Grade Converter")
choice = "y"
while choice.lower() == "y":
    try:
        grade = int(input("\nEnter numerical grade: "))    
        letter_grade = Grade.get_letter(grade)
        print(f"Letter grade: {letter_grade}")
    except ValueError:
        print("Please enter a whole number.")
    choice = input("\nContinue? (y/n): ")

