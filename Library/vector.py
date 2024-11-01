from math import atan, pi, sqrt
class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def normalize(self):
        return self/self.length

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    """
    * Contribution by @aminskey.
    """
    @property
    def polar(self):
        return atan(self.__y/self.__x)
    @property
    def polar360(self):
        if self.__x > 0:
            return atan(self.__y / self.__x)
        elif self.__x < 0:
            return atan(self.__y / self.__x) + pi
        else:
            return 0

    @property
    def length(self):
        return sqrt(self.__y**2 + self.__x**2)

    def limit(self, l):
        return self.normalize() * l

    def __str__(self):
        return f"Vector; x={self.__x}, y={self.__y}"

    def __add__(self, other):
        return Vector(self.__x + other.__x, self.__y + other.__y)

    def __sub__(self, other):
        return Vector(self.__x - other.__x, self.__y - other.__y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.__x * other.__x, self.__y * other.__y)
        if isinstance(other, float) or isinstance(other, int):
            return Vector(self.__x * other, self.__y * other)

    def __truediv__(self, other):
        if isinstance(other, Vector):
            return Vector(self.__x / other.__x, self.__y / other.__y)
        if isinstance(other, float) or isinstance(other, int):
            return Vector(self.__x / other, self.__y / other)