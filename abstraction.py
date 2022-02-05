'''Creating a program using classes to explain 
   abstraction concept.
'''

class WashingMachine():

    def __init__(self):
        pass
    
    def washing(self, temperature='hot'):
        self._fill_water_tank(temperature)
        self._add_soap()
        self._washing()
        self._centrifuge()
    
    def _fill_water_tank(self, temperature):
        print(f'Filling tank with {temperature} water.')

    def _add_soap(self):
        print('Adding soap.')
    
    def _washing(self):
        print('Washing colthes.')
    
    def _centrifuge(self):
        print('Centrifuging clothes.')
    

if __name__=='__main__':
    washing_machine = WashingMachine()
    washing_machine.washing()

