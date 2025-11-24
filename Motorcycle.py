# Motorcycle.py

class Motorcycle(Vehicle):

    def __init__(self):
        super().__init__("Motorcycle")
        
    def start_engine(self):
        print("Motorcycle Engine started ===> Vroom Vroom!")

