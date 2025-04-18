#max/min
nbr1 = 5
nbr2 = 12
print(f'max is: {max(nbr1, nbr2)}')
nbr3 = 17
print(f'max is: {max(nbr1, nbr2, nbr3)}')

#sum
print(f'sum is: {sum([nbr1, nbr2, nbr3])}')

#round
pi = 3.14152
print(f'round pi: {round(pi, 2)}')

# random
import random as rand
print(f'random nbr: {rand.random()}')
print(f'die roll: {rand.randint(1,6)}')

#formatting
price = 26789
price_currency = "${:,.2f}".format(price)
print(f'price = {price_currency}')
grade = .9995
grade_pct_1 = format(grade,'%')
print(grade_pct_1)
grade_pct_2 = '{:.2%}'.format(grade)
print(grade_pct_2)
print(f'Format % w/ 2 decimals: {grade:.2%}')

