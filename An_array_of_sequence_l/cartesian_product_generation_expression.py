colors = ['Black', 'White']
sizes = ['S', 'M', 'L']

tshirts = (f'{c} {s}' for c in colors for s in sizes)
for tshirt in tshirts:
    print(tshirt)