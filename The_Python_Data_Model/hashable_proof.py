def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True

fake_tuple = (1,2,3,4,'Hello', ['Manzana', 'Mango'])
real_tuple = (1,2,3,4, 'Hello', ('Manzana', 'Mango'))

print(f"Fake tuple is {fixed(fake_tuple)}")
print(f"Real tuple is {fixed(real_tuple)}")
