from typing import List
from infrastructure.interfaces.ivehicle_manager import IVehicleManager
from infrastructure.factories.vehicle_factory import VehicleFactory
from model.data_classes.vehicle import Vehicle
from globals.consts.logger_messages import LoggerMessages
from infrastructure.factories.logger_factory import LoggerFactory
from globals.consts.const_strings import ConstStrings

class VehicleManager(IVehicleManager):
    def __init__(self):
        self._vehicles: List[Vehicle] = []
        self._logger = LoggerFactory.get_logger_manager()

    def create_vehicle(self, vehicle_type: str):
        vehicle = VehicleFactory.create(vehicle_type)
        if vehicle:
            self._vehicles.append(vehicle)
            self._logger.log(ConstStrings.LOG_NAME_DEBUG,LoggerMessages.VEHICLE_CREATED_SUCCESS.format(vehicle_type))
           # print(f"{vehicle_type} created successfully.")
        else:
            self._logger.log(ConstStrings.LOG_NAME_ERROR,LoggerMessages.VEHICLE_CREATION_FAILED.format(vehicle_type))
            #print(f"Failed to create vehicle of type: {vehicle_type}")

    def start_all(self):
        if not self._vehicles:
            print("No vehicles created.")
            return
        
        self._logger.log(ConstStrings.LOG_NAME_DEBUG,LoggerMessages.VEHICLE_STARTING_ALL)
        #print("\nStarting all engines...\n")
        for v in self._vehicles:
            v.start_engine()

