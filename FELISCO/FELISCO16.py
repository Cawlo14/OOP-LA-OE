class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def operate(self):
        print("Operating!")

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class WashingMachine(Appliance):
    def operate(self):
        print("Washing clothes!")

class Refrigerator(Appliance):
    def operate(self):
        print("Keeping food cold!")

class Microwave(Appliance):
    def operate(self):
        print("Heating food!")

washing_machine = WashingMachine("LG", "Frontload")
refrigerator = Refrigerator("Samsung", "SMS201324")
microwave = Microwave("Panasonic", "PNS23002")

appliances = [washing_machine, refrigerator, microwave]

for appliance in appliances:
    appliance.operate()
    appliance.info()