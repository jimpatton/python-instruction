print('Welcome to the travel time calculator')
choice = 'y'
while choice =='y':
    miles = int(input('Enter miles: '))
    mph = int(input('Enter miles per hour: '))
    time= miles/mph
    hours = int(time)
    minutes = (time-hours)*60
    print('Estimated travel time')
    print(f"Hours: {hours}")
    print(f'Minutes: {round(minutes)}')
    choice = input('Continue? (y/n): ')