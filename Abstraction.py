from abc import ABC, abstractmethod

# create Shape class give it access to ABC
class Shape(ABC):
    # define info function 
    def info(self, shape):
        print('This object is a ',shape)
    # define area function using abstractmethod decorator
    @abstractmethod
    def area(self):
        pass
# create Rectangle as a subclass of Shape
class Rectangle(Shape):
    # def __init__ constructor and ask for length, width
    def __init__(self, length, width):
        self.l = length
        self.w = width
    # defining how to impliment area from its parent Shape class
    def area(self):
        return self.l * self.w

r = Rectangle(15,25)
r.info('rectangle')
print('area: ',r.area())



        
