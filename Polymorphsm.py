class Vehicle:
    def __init__(self, a, b, c):
        self.make=a
        self.model=b
        self.year=c
    def display(self):
        print("Vehicle Make:", self.make)
        print("Vehicle Model:", self.model)
        print("Vehicle Year:", self.year)
        return ""
class Car(Vehicle):
    def __init__(self, a = "", b = "", c = "", z= ""):
        Vehicle.__init__(self, a, b, c)
        self.tcap = z
class Truck(Vehicle):
    def __init__(self, a = "", b = "", c = "", z = ""):
        Vehicle.__init__(self, a, b, c)
        self.tcap = z
    def display(self):
        print(Vehicle.display(self))
        print("Towing Capacity:", self.tcap)