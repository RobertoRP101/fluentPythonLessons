import math
# Author's example
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 100]
print(beyond_ascii)
beyond_ascii = list(filter(lambda c: c > 100, map(ord, symbols)))
print(beyond_ascii)

# My example
def is_sqrt(number):
    return math.isqrt(number)**2 == number

sqrtable_numbers = [last := (number) for number in range(0,101,1) if is_sqrt(number)]
print(sqrtable_numbers)
sqrtable_numbers = list(filter(lambda number: is_sqrt(number) , map(int, range(0,101,1)) ))
print(sqrtable_numbers)