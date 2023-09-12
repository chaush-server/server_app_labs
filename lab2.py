# TAXI
class TaxiCompany:
    def __init__(self, name, cars):
        self.name = name
        self.cars = cars

    def sort_by_fuel_consumption(self):
        self.cars = sorted(self.cars, key=lambda car: car.fuel_consumption)

    def find_by_speed(self, speed):
        return list(filter(lambda car: car.speed == speed, self.cars))

    def __repr__(self):
        return str(self.cars)


class Car:
    def __init__(self, name, speed, fuel_consumption):
        self.name = name
        self.speed = speed
        self.fuel_consumption = fuel_consumption

    def __repr__(self):
        return f'[{self.name}, {self.speed}, {self.fuel_consumption}]'


class PassengerCar(Car):
    def __init__(self, name, speed, fuel_consumption, max_passengers):
        super().__init__(name, speed, fuel_consumption)
        self.max_passengers = max_passengers


class Truck(Car):
    def __init__(self, name, speed, fuel_consumption, max_load):
        super().__init__(name, speed, fuel_consumption)
        self.max_load = max_load


def main():
    cars = [
        PassengerCar('BMW', 200, 7, 5),
        PassengerCar('Mercedes', 220, 8, 2),
        PassengerCar('Lada', 180, 5, 5),
        Truck('Men', 180, 4, 1),
        Truck('Toyota', 210, 5, 2),
        Truck('Volvo', 200, 6, 5),
    ]
    company = TaxiCompany('See-Taxi', cars)
    print('Unsorted: ', company)
    company.sort_by_fuel_consumption()
    print('Sorted by fuel consumption:', company)
    print('Found by speed 200: ', company.find_by_speed(200))


if __name__ == '__main__':
    main()
