# Vehicle.py

from abc import ABC, abstractmethod

class Vehicle(ABC):

    type_name = ""
    def __init__(self, vehicle_type):
        self.type_name = vehicle_type
        

    @abstractmethod
    def start_engine(self):
        pass