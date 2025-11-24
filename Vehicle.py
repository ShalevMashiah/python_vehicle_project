# Vehicle.py

from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, vehicle_type):
        self.make = vehicle_type


    @abstractmethod
    def start_engine(self):
        pass