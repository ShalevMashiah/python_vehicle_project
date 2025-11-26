# main.py
from model.managers.vehicle_manager import VehicleManager
from globals.enums.vehicle_enums import VehicleEnums

def main():
    manager = VehicleManager()

    manager.create(VehicleEnums.CAR.value)
    manager.create(VehicleEnums.TRUCK.value)
    manager.create(VehicleEnums.MOTORCYCLE.value)

    # manager.start_all()


if __name__ == "__main__":
    main()

