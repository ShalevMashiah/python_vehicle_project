# Truck.py

from .vehicle import Vehicle

class Truck(Vehicle):

    type_name = "truck"
    
    def __init__(self):
        super().__init__("Truck")
        
    def start_engine(self):
        print("Truck Engine started ===> Vroom Vroom!")

