# vehicle_manager.py

from infrastructure.factories.vehicle_factory import VehicleFactory


class VehicleManager:
    def __init__(self, factory: VehicleFactory | None = None):
        self.vehicles = []
        self.factory = factory or VehicleFactory()

    def create(self, vehicle_type: str):
        vehicle = self.factory.create_and_start(vehicle_type)
        if vehicle:
            self.vehicles.append(vehicle)
    def start_all(self):
        if not self.vehicles:
            print("No vehicles created.")
            return

        print("\nStarting all engines again from manager...\n")
        for v in self.vehicles:
            v.start_engine()
