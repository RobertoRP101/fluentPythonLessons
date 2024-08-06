import math

class Vector(object):
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f'Vector({self.x!r}, {self.y!r})'
    
    def __abs__(self) -> int:
        return math.hypot(self.x, self.y)
    
    def __bool__(self) -> bool:
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)
    
    def __mul__(self, scalar):
        x = self.x * scalar
        y = self.y * scalar
        return Vector(x,y)