#
#   Python:     3.9.7    
#
#   Author:     Matt Fuller
#
#   Purpose:    Create one parent class with two child classes.
#               Child classes should use polymorphism on the parent class method



# create parent class
class Vehicle:
    make = ''
    model = ''
    year = None
    engine = ''

    # define init function
    def __init__(self,make,model,year,engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine

    # define info function
    def info(self):
        msg = '\nMake: {}\nModel: {}\nYear: {}\nEngine: {}'.format(self.make,self.model,self.year,self.engine)
        return msg


# child class instance
class Truck(Vehicle):
    
    # define init function using super() to inherit Vehicle attributes
    def __init__(self,make,model,year,engine,wd,towing_capacity):
        super(Truck,self).__init__(make,model,year,engine)
        self.wd = wd
        self.towing_capacity = towing_capacity

    # This is the same method in the parent class 'Vehicle' but adds wd and towing_capacity attributes
    def info(self):
        msg = '\nMake: {}\nModel: {}\nYear: {}\nEngine: {}\n4WD: {}\nTowing Capacity: {}'.format\
              (self.make,self.model,self.year,self.engine,self.wd,self.towing_capacity)
        return msg


# child class instance
class Boat(Vehicle):
    displacement = 0
    number_of_hulls = 1

    # define init function using super() to inherit Vehicle attributes
    def __init__(self,make,model,year,engine,displacement,number_of_hulls):
        super(Boat,self).__init__(make,model,year,engine)
        self.displacement = displacement
        self.number_of_hulls = number_of_hulls 

    # This is the same method in the parent class 'Vehicle' but adds displacement and number of hulls attributes
    def info(self):
        msg = '\nMake: {}\nModel: {}\nYear: {}\nEngine: {}\nDisplacement: {}\nNumber of Hulls: {}'.format\
              (self.make,self.model,self.year,self.engine,self.displacement,self.number_of_hulls)
        return msg
    
    

if __name__ == '__main__':
    
    x = Vehicle('toyota','4runner',2021,'v6')

    print(x.info())
    

    y = Truck('ford','f-150',2019,'v6',True,'18000')

    print(y.info())
    

    z = Boat('Bavaria','C38',2022,'50hp',19996,1)

    print(z.info())
  

