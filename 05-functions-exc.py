def add_function(num1, num2):
    return num1 + num2

print(add_function(4,23))

def subtract_function(num1, num2=0):
    return num1-num2
print(subtract_function(56,22))
print(subtract_function(43))
print(subtract_function(56, num2=14))

def add(*nbrs):
    sum=0
    for n in nbrs:
        sum += n
    return sum

print(add(2,2))
print(add(2,4,6,8))

#keyword arguments or kwargs
def calc_total_function(price, qty, handling_fee):
    #(price*qty)+handling fee
    return(price*qty)+handling_fee
print("total: ",calc_total_function(20,2,3))
print("total2: ",calc_total_function(20,3,2))
print("total3: ",calc_total_function(handling_fee=5, qty=7, price=10))

#exceptions
while True:    
    try:
        whole_number = int(input('Enter a whole number: '))
        print(f'You entered the number {whole_number}')
        break
    except ValueError:
        print('Invalid entry')