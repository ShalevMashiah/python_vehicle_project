from infrastructure.interfaces.ivehicle_manager import IVehicleManager
from model.managers.vehicle_manager import VehicleManager
from globals.enums.vehicle_enums import VehicleEnums

class ManagerFactory:
    @staticmethod
    def create_vehicle_manager() -> IVehicleManager:
        return VehicleManager()

    @staticmethod
    def create_all() -> None:
        vehicle_manager = ManagerFactory.create_vehicle_manager()

        vehicle_manager.create_vehicle(VehicleEnums.CAR.value)
        vehicle_manager.create_vehicle(VehicleEnums.TRUCK.value)
        vehicle_manager.create_vehicle(VehicleEnums.MOTORCYCLE.value)

        vehicle_manager.start_all()