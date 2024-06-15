# Base Class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Vehicle:{self.make},{self.model},{self.year}")


# Derived Class Single Inheritance -> Car inherits from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Car with {self.num_doors} doors")


print(" ---- This Single Inheritance ----")
car = Car("Toyato", "Toyato2.0", 2024, 4)
car.display_info()
print()


# Multiple Inheritance
class Electric:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def display_info(self):
        print(f"Electric car with {self.battery_capacity} kwh")


class Fuel:
    def __init__(self, fuel_capacity):
        self.fuel_capacity = fuel_capacity

    def display_info(self):
        print(f"Fuel capacity is {self.fuel_capacity} lilters")


class HybridCar(Car, Electric, Fuel):
    def __init__(self, model, year, battery_capacity, fuel_capacity):
        Car.__init__(self, model=model, year=year, make=None, num_doors=None)  # since we dont need all
        Electric.__init__(self, battery_capacity)
        Fuel.__init__(self, fuel_capacity)

    def display_info(self):
        # Car.display_info(self) -> it will give you unwanted so we gotta modify
        print(f"Hybrid Car : Model {self.model}, Year: {self.year}")
        Electric.display_info(self)
        Fuel.display_info(self)


print(" --- Multiple Inheritance ---")
hybrid_car = HybridCar("Toyato2.0", 2024, "good", "better")
hybrid_car.display_info()
print()


# Multilevel inheritance
class Truck(Vehicle):
    def __init__(self, make, model, year, load_capacity):
        self.load_capacity = load_capacity
        super().__init__(make, model, year)

    def display_info(self):
        super().display_info()
        print(f" The load capacity is {self.load_capacity} ")


class Pickup_truck(Truck):
    def __init__(self, make, model, year, load_capacity, cab_type):
        super().__init__(make, model, year, load_capacity)
        self.cab_type = cab_type

    def display_info(self):
        super().display_info()
        print(f"Pickup Truck with {self.cab_type} cab")


print(" --- Multilevel Inheritance --- ")
pickup_truck = Pickup_truck("Toyata2.0", "new", 2024, "F-150", "Double")
pickup_truck.display_info()
print()


# Hierarchical Inheritance

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type):
        super().__init__(make, model, year)
        self.type = type

    def display_info(self):
        super().display_info()
        print(f"this type is {self.type}")


class Bus(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year)
        self.color = color

    def display_info(self):
        super().display_info()
        print(f"color is {self.color}")


print(" -- Hierarchical Inheritance -- ")
bus = Bus("Toyata2.0", "Brand New", 2024, "red")
bus.display_info()

motor_cycle = Motorcycle("12", "new", 2023, "a.0")
motor_cycle.display_info()