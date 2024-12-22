class Toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_details(self):
        print(f"Toy Name: {self.name}, Price: P{self.price}")

class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)

my_car = Car("CR Helicopter", 12.92)

my_car.display_details()