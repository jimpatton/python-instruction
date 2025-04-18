#Arrays
even_numbers = [2,4,6,8,10]
odd_numbers = [1,3,7,9]

#add value at the end
even_numbers.append(12)

#add value at index position
odd_numbers.insert(2,5)

print(f'Even nums: {even_numbers}')
print(f'Odd nums: {odd_numbers}')

#for loops with range
numbers = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(numbers)):
    print(f'{i}: {numbers[i]}')

#by 2s
for i in range(0,11,2):
    print(f'{i}', end=', ')
print()

# iterate over numbers using enumerate
#so we can get an index too
for idx, value in enumerate(numbers):
    print(f'{idx}, {value}')