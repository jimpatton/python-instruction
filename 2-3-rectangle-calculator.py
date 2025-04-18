print('Welcome to the rectangle calculator')
choice = 'y'
while choice =='y':
    length = float(input('Enter length: '))
    width = float(input('Enter width: '))
    area = length* width
    perimeter = (2*length) + (2*width)
    print('Area =' + str(area))
    print('Perimeter = '+ str(perimeter))
    choice = input('Continue? y/n ')
