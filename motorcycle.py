# Motorcycle.py

from vehicle import Vehicle

class Motorcycle(Vehicle):

    type_name = "motorcycle"
    
    def __init__(self):
        super().__init__("Motorcycle")
        
    def start_engine(self):
        print("Motorcycle Engine started ===> Vroom Vroom!")

