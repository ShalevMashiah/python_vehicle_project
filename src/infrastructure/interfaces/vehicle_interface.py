from abc import ABC, abstractmethod

class IVehicleFactory(ABC):
    @abstractmethod
    def create(self, vehicle_type: str):
        pass

    @abstractmethod
    def create_and_start(self, vehicle_type: str):
        pass