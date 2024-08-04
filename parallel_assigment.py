lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates #unpacking
print(latitude)
print(longitude)


# Initial values
a = 5
b = 10

# Swapping values using tuple unpacking
b, a = a, b

# Values after swapping
print(f"a = {a}")  
print(f"b = {b}")  


t = (20, 8)
divmod(*t)

quotient, remainder = divmod(*t)
print(f'{quotient} {remainder}')
print((quotient,remainder))
