#vehicle_manager

from typing import List
from infrastructure.interfaces.ivehicle_manager import IVehicleManager
from infrastructure.factories.vehicle_factory import VehicleFactory
from model.data_classes.vehicle import Vehicle


class VehicleManager(IVehicleManager):
    def _init_(self):
        self._vehicles: List[Vehicle] = []

    def create_vehicle(self, vehicle_type: str):
        vehicle = VehicleFactory.create(vehicle_type)
        if vehicle:
            self._vehicles.append(vehicle)
            print(f"{vehicle_type} created successfully.")
        else:
            print(f"Failed to create vehicle of type: {vehicle_type}")

    def start_all(self):
        if not self._vehicles:
            print("No vehicles created.")
            return

        print("\nStarting all engines...\n")
        for v in self._vehicles:
            v.start_engine()