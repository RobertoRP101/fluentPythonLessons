a, b, c, *rest = range(1,11,1)
print(f'{a}, {b}, {c}, {rest}')

a, b, *rest = range(5)
print(f'{a}, {b}, {rest}')

a, b, *rest = range(2)
print(f'{a}, {b}, {rest}')
