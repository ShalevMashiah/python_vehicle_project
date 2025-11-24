# Car.py

class Car(Vehicle):

    def __init__(self):
        super().__init__("Car")
        
    def start_engine(self):
        print("Car Engine started ===> Vroom Vroom!")

