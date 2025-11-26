from model.data_classes.vehicle import Vehicle
from model.data_classes.car import Car          
from model.data_classes.truck import Truck
from model.data_classes.motorcycle import Motorcycle


class VehicleFactory:
    @staticmethod
    def create(vehicle_type: str) -> Vehicle | None:
        type_name = vehicle_type.lower()

        for cls in Vehicle._subclasses_():
            if cls.type_name.lower() == type_name:
                return cls()

        print(f"Vehicle type '{vehicle_type}' is not recognized.")
        return None