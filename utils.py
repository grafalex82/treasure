class Pos:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    def __eq__(self, other):
        return self._x == other._x and self._y == other._y
    
    def __hash__(self):
        return hash((self._x, self._y))
        
    def below(self):
        return Pos(self._x, self._y + 1)
    
    def above(self):
        return Pos(self._x, self._y - 1)

    def left(self):
        return Pos(self._x - 1, self._y)

    def right(self):
        return Pos(self._x + 1, self._y)
