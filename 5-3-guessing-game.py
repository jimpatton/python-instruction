def get_valid_integer(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Error! Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Error! Please enter a whole number.")

def main():
    print('Welcome to the guessing game')
    print("\nI'm thinking of a number between 1 and 100.\nTry to guess it.")
    choice = 'y'.lower()
    while choice.lower() =='y':
        import random as rand
        nbr = int(rand.randint(1,101))
        guess = 0
        count = 0
        while (guess != nbr):
            count += 1    
            guess = get_valid_integer('\nEnter number: ',1,100)
            if guess==nbr:
                print(f"You guessed it in {count} tries")
                if count <= 3:
                    print("Great work! You are a mathematical genius!")
                elif count <= 7:
                    print("Not too bad. You've got some potential.")
                elif count > 7:
                    print('What took you so long? You should be ashamed!')
            elif guess >= nbr +10:
                print('Way too high!')
            elif guess > nbr:
                print('Too high')
            elif guess <= nbr -10:
                print('Way too low')
            elif guess < nbr:
                print('Too low')
        choice = input('\nTry again? ')
if __name__ == "__main__":
    main()