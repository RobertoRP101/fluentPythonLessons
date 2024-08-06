import math

# cartesian product

pens = ['Azor', 'Bic']
colors = ['Blue', 'Black', 'Red']

list_pens = [(pen,color) for pen in pens for color in colors]
print(list_pens)

# listcomps vs filter/map

numbers_map = list(filter(lambda number: number, map(math.exp2,range(0,101,1))))
print(f'Filter/Map:\n{numbers_map}')

numbers_list = [ math.exp2(number) for number in range(0,101,1)]
print(f'List comprehension:\n{numbers_list}')

# listcomps

odd_numbers = [last := number for number in range(0,101,1) if number%2==0]
print(odd_numbers)
print(f'Last element: {last}')


# local_scope

even_number = [number for number in range(0,101,1) if number%2!=0]
print(even_number)

# parrallel_assigment

books = ('Python', 'Java')
masters, beginners = books
print(masters)
print(beginners)

first, second, *rest = range(11)
print(first)
print(second)
print(rest)


# Hasable

def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True
    
print(fixed(range(0,11,1)))


tuple_numbers = tuple(range(0,11,1))
list_numbers = list(range(11,21,1))
numbers = tuple((tuple_numbers, *list_numbers))
print(fixed(numbers))