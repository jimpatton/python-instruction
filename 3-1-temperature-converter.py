print('Temperature Converter')
choice = 'y'
while choice == 'y':
    tempf = float(input('Enter degrees in Fahrenheit: '))
    tempC = (tempf - 32) *5/9
    print(f'Degrees in Celsius: {round(tempC,2)}')
choice =input('Continue y/n?' )

