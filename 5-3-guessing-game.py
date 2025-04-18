print('Welcome to the guessing game')
print("I'm thinking of a number between 1 and 100.\nTry to guess it.")
choice = 'y'.lower()
while choice =='y':
    import random as rand
    nbr = int(rand.randint(1,101))
    guess = 0
    count = 0
    while (guess != nbr):
        count += 1    
        guess = int(input('Guess number: '))
        if guess==nbr:
            print(f"You guessed it in {count} tries")
            if count < 3:
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
    choice = input('Try again? ')