# main.py

from model.data_classes.car import Car as car
from model.data_classes.motorcycle import Motorcycle
from model.data_classes.truck import Truck as truck
from infrastructure.factories.vehicle_factory import Vehicle_Factory 

def main():
    V1 = car()
    V2 = truck()
    V3 = Motorcycle()
    V1.start_engine()
    V2.start_engine()
    V3.start_engine()
    print("\nCreating vehicles using Factory:\n")
    
    types = ["car", "truck", "motorcycle", "sgjfnfsgjn"]
    vehicles = []

    for type in types:
        vehicles.append(Vehicle_Factory.create(type))
        
    for vehicle in vehicles:
        if vehicle:
            vehicle.start_engine()

if __name__ == "__main__":
    main()
