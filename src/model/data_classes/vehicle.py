# Vehicle.py

from abc import ABC, abstractmethod

class Vehicle(ABC):
    type_name: str = ""

    def __init__(self, vehicle_type: str):
        self.type_name = vehicle_type

    @abstractmethod
    def start_engine(self):
        pass
