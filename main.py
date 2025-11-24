# main.py

from car import Car
from factory import Factory
from truck import Truck
from motorcycle import Motorcycle

def main():
    V1 = Car()
    V2 = Truck()
    V3 = Motorcycle()
    V1.start_engine()
    V2.start_engine()
    V3.start_engine()
    print("\nCreating vehicles using Factory:\n")
    
    types = ["car", "truck", "motorcycle", "sgjfnfsgjn"]
    vehicles = []

    for type in types:
        vehicles.append(Factory.create(type))
        
    for vehicle in vehicles:
        if vehicle:
            vehicle.start_engine()

if __name__ == "__main__":
    main()
