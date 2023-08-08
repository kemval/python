class Person:
    def __init__(self, name, license_type, car):
        self.name = name
        self.license_type = license_type
        self.driving = False
        self.car = car
    """
    Person attributes: type of license, name, driving, car
    Person methods: drive, start_car
    """
    def person_name (self,person_name):
        self.name=person_name
    
    def license_type (self, license_type):
        self.license_type = license_type

    def is_driving (self):
        self.driving = True

    def person_car (self):
        self.car = Car("TOYOTA")

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.on = False
        self.speed = 0
    
    def start(self):
        self.on = True
    
    def turn_off(self):
        self.on = False
    
    def accelerate(self):
        self.speed += 5
    
    def stop(self):
        while self.speed > 0:
            self.speed -= 5
    
    def brake(self):
        self.speed -= 5
    """
    Car attributes: brand, on, speed
    Car methods: start, turn_off, accelerate, stop. 
    """
