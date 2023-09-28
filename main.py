import matplotlib.pyplot as plt

class Automobile():

    number_of_doors = 2

    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def __repr__(self):
        return f"""Automobile Data:
Year of manufacture : {self.year}
Automobile make     : {self.make}
Automobile model    : {self.model}"""


class Truck(Automobile):

    def __init__(
        self, year, make, model, bed_type, bed_size, axel_weight
    ):
        super().__init__(year, make, model)
        self.bed_type = bed_type
        self.bed_size = bed_size
        self.axel_weight = axel_weight


class Sedan(Automobile):

    number_of_doors = 4

    def __init__(self, year, make, model, engine_type, engine_size):
        super().__init__(year, make, model)
        self.engine_type = engine_type
        self.engine_size = engine_size


class Coupe(Automobile):

    def __init__(self, year, make, model, engine_type, engine_size):
        super().__init__(year, make, model)
        self.engine_type = engine_type
        self.engine_size = engine_size


class Corvette(Coupe):

    def __init__(self, year, edition, engine_size):
        super().__init__(
            year, "Chevrolet", "Corvette", "V8", engine_size
        )
        self.edition = edition

    def __repr__(self):
        return f"""This car is a {self.make} {self.model},"""\
               f""" {self.edition} Edition made in {self.year}.
It has a {self.engine_size} cubic-inch {self.engine_type} engine."""\
            f"""It is awesome!!!"""


t = Truck(1990, "Ford", "F-250", "Flat", "Long (8')", '3/4 Ton')
s = Sedan(2017, "Hyundai", "Elantra", 'Straight 4', 92)
p = Coupe(2012, "Toyota", "Camry", "V6", 205)
c = Corvette(1975, "Sting Ray", 350)


automobiles = [t, s, p, c]
types = ["Truck", "Sedan", "Coupe", "Corvette"]
doors = [car.number_of_doors for car in automobiles]

plt.bar(types, doors)
plt.xlabel("Automobile Type")
plt.ylabel("Number of Doors")
plt.title("Number of Doors by Automobile Type")
plt.show()


