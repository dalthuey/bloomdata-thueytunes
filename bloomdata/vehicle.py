'''
This is a file that holds two classes. A parent and child class relationship
'''

class Vehicle:

    '''
    This is a vehicle class
    '''

    def __init__(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def honk(self):
        '''
        Honks horn
        '''
        return "HOOOOOOOOOOONK"
    
    def drive(self, miles_driven):
        '''
        Adds miles_driven to initial mileage count
        '''
        self.mileage += miles_driven
        return self.mileage
    
    def __repr__(self):
        return f"A {self.color} {self.year} {self.make} {self.model} with {self.mileage} miles"

class Convertible(Vehicle):
    '''
    This is a convertible class
    '''

    def __init__(self, make, model, color, year, mileage, top_down= True):
        super().__init__(make, model, color, year, mileage)
        self.top_down = top_down

    def change_top_status(self):
        '''
        Chages Top Status
        '''
        if self.top_down:
            self.top_down= False
            return "Top is now up"
           
        self.top_down= True
        return "Top is now down"
    
    def __repr__(self):
        return f"A {self.color} {self.year} {self.make} {self.model} convertible with {self.mileage} miles"
