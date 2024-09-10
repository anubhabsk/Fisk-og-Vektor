import pygame

from math import sqrt

class Vector:
    numOfVectors = 0

    def __init__(self, x, y):
        global numOfVectors
        self.__x = x
        self.__y = y
    
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
    
    