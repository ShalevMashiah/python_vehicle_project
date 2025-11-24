# factory.py

from vehicle import Vehicle


class Factory:

    @staticmethod
    def create(vehicle_type):
       type_name = vehicle_type.lower()

       for i in Vehicle.__subclasses__():
           if i.type_name.lower() == type_name:
               return i()
       
       print(f"Vehicle type '{vehicle_type}' is not recognized.")
       return None
    
    