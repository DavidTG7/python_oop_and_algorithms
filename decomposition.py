''' Basic model for decomposition, we take a car as
    initial main object, however it can be decomposed
    into other simpler objects.
'''

class Car:

    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.colo = color
        self._stauts = 'quiet'
        self._motor = Motor(cylinders=4)

    def acceleration(self, type1='slow'):
        if type1 == 'fast':
            self._motor.inject_gasoline(10)
        else:
            self._motor.inject_gasoline(3)
        
        self._status = 'moving'
    
class Motor:

    def __init__(self, cylinders, type='gasoline'):
        self.cylinders = cylinders
        self.type = type
        self._temperature = 0

    def inject_gasoline(self, amount):
        pass
    

    