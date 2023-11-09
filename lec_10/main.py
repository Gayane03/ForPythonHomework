from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print('Car class')
        

class Plane(Vehicle):
    def __init__(self):
        super().__init__()
        print('Plane class')
        

class Boat(Vehicle):
    def __init__(self):
        super().__init__()
        print('Boat class')


class RaceCar(Car):
    def __init__(self):
        super().__init__()
        print('RaceCar class')

vehicle=Vehicle()
car = Car()
plane = Plane()
boat = Boat()
race_car = RaceCar()
