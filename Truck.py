# Truck.py

class Truck(Vehicle):

    def __init__(self):
        super().__init__("Truck")
        
    def start_engine(self):
        print("Truck Engine started ===> Vroom Vroom!")

