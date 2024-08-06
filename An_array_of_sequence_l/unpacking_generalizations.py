def unpacking(a, b, c, d, *rest):
    return a, b, c, d, rest


print(unpacking((2,4), 4, 5, (5, 9, 6, 4)))