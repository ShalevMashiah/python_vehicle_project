# main.py


from car import Car
from truck import Truck
from motorcycle import Motorcycle

def main():
    V1 = Car()
    V2 = Truck()
    V3 = Motorcycle()
    V1.start_engine()
    V2.start_engine()
    V3.start_engine()

if __name__ == "__main__":
    main()
