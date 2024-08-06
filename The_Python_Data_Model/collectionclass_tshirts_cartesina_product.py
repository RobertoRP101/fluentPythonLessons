import collections

numbers_squared = [last := x**2 for x in range(0,101)]
print(last)
print(numbers_squared)

Tshirt = collections.namedtuple('Tshirt', ['color', 'size'])

class TshirtsAvailables(object):
    color = ['black', 'white']
    size = ['S','M','L']
    
    def __init__(self) -> None:
        self.Tshirts = [Tshirt(color, size) for color in self.color for size in self.size]
    
    def __len__(self) -> int:
        return len(self.Tshirts)
    
    def __getitem__(self, position) -> Tshirt:
        return self.Tshirts[position]
    
    def __repr__(self) -> str:
        return f'{self.Tshirts}'
    
    
tshirts_available = TshirtsAvailables()
print(tshirts_available)
print(len(tshirts_available))
for tshirt in tshirts_available:
    print(tshirt)