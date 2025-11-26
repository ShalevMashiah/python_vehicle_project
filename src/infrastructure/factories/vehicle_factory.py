# vehicle_factory.py
from model.data_classes.vehicle import Vehicle
from model.data_classes.car import Car
from model.data_classes.truck import Truck
from model.data_classes.motorcycle import Motorcycle
from infrastructure.interfaces.vehicle_interface import IVehicleFactory

class VehicleFactory(IVehicleFactory):

    def create(self, vehicle_type: str):
        type_name = vehicle_type.lower()

        for cls in Vehicle.__subclasses__():
            if cls.type_name.lower() == type_name:
                return cls()

        print(f"Vehicle type '{vehicle_type}' is not recognized.")
        return None

    def create_and_start(self, vehicle_type: str):
        vehicle = self.create(vehicle_type)
        if vehicle:
            vehicle.start_engine()
        return vehicle
