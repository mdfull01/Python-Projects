from abc import ABC, abstractmethod


class Shape(ABC):
    def info(self, shape):
        print('This object is a ',shape)

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.l = length
        self.w = width
    def area(self):
        return self.l * self.w

r = Rectangle(15,25)
r.info('rectangle')
print('area: ',r.area())



        
