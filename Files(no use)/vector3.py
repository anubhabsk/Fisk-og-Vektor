class Vector:
    def __init__(self, x, y):
        self._x = x
        self._y = y



    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value



    def __str__(self):
        return f"Vector; x={self._x}, y={self._y}"

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def __sub__(self, other):
        return Vector(self._x - other._x, self._y - other._y)

    def __mul__(self, other):
        return Vector(self._x * other._x, self._y * other._y)

    def __truediv__(self, other):
        return Vector(self._x / other._x, self._y / other._y)