# Car.py

from .vehicle import Vehicle

class Car(Vehicle):

    type_name = "car"
    def __init__(self):
        super().__init__("Car")
        
    def start_engine(self):
        print("Car Engine started ===> Vroom Vroom!")

