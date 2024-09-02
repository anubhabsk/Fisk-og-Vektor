class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def getx(self):
        return self.__x
    
    def gety(self):
        return self.__y
    
    def setx(self, x):
        self.__x = x
    
    def sety(self, y):
        self.__y = y
    
    

    def __str__ (self):
        return f"Vector; x={self.__x}, y={self.__y}"
    
    def __add__ (self, other):
        return Vector(self.__x + other.__x, self.__y + other.__y)
    
    def __sub__ (self, other):
        return Vector(self.__x - other.__x, self.__y - other.__y)
    
    def __mul__ (self, other):
        return Vector(self.__x * other.__x, self.__y * other.__y)
    
    def __truediv__ (self, other):
        return Vector(self.__x / other.__x, self.__y / other.__y)
        

v, v2 = Vector(3, 1), Vector(4,5)
print(v)
print(v2)
print(v + v2)
print(v - v2)
print(v * v2)
print(v / v2)