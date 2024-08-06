# Author's example
colors = ['Black', 'White']
sizes = ['S', 'M', 'L']

tshirt = [(color, size) for color in colors for size in sizes]
print(tshirt)

for color in colors:
    for size in sizes:
        print((color, size))
        
        
# My example       
colors = ['Red', 'Blue', 'Yellow', 'Green']
sizes = list(range(7,16,1))

ballons = [last := (color, size) for color in colors for size in sizes]
print(ballons)
print(f'Last: {last}')
for color in colors:
    for size in sizes:
        print((color, size))

