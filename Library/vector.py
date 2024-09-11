from math import atan, pi
class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y


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


    def __str__(self):
        return f"Vector; x={self.__x}, y={self.__y}"

    def __add__(self, other):
        return Vector(self.__x + other.__x, self.__y + other.__y)

    def __sub__(self, other):
        return Vector(self.__x - other.__x, self.__y - other.__y)

    def __mul__(self, other):
        return Vector(self.__x * other.__x, self.__y * other.__y)

    def __truediv__(self, other):
        return Vector(self.__x / other.__x, self.__y / other.__y)