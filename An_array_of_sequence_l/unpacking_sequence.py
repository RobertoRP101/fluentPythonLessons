lax_coordinates = (23.3432, -235.2344231)
latitude, longitude = lax_coordinates

# Important

quotient, remainder = divmod(20,8)
print(quotient)
print(remainder)


tuple_numbers = (20,8)
print(divmod(*tuple_numbers))


import os

_, filename = os.path.split('Fluent python\Lessons\An_array_of_sequence_l')
print(filename)