#quiz1

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

if __name__ == "__main__":
    new_car = Car(registration_number="ABC-123", maximum_speed=142)

    print("Registration Number:", new_car.registration_number)
    print("Maximum Speed:", new_car.maximum_speed, "km/h")
    print("Current Speed:", new_car.current_speed, "km/h")
    print("Travelled Distance:", new_car.travelled_distance, "km")

#quiz2

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        if speed_change < 0:
            self.current_speed = max(0, self.current_speed + speed_change)
        else:
            self.current_speed = min(self.maximum_speed, self.current_speed + speed_change)

if __name__ == "__main__":
    new_car = Car(registration_number="ABC-123", maximum_speed=142)

    new_car.accelerate(30)
    new_car.accelerate(70)
    new_car.accelerate(50)

    print("Current Speed:", new_car.current_speed, "km/h")


    new_car.accelerate(-200)

    print("Final Speed after emergency brake:", new_car.current_speed, "km/h")

#quiz3

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        if speed_change < 0:
            self.current_speed = max(0, self.current_speed + speed_change)
        else:
            self.current_speed = min(self.maximum_speed, self.current_speed + speed_change)

    def drive(self, hours):
        distance_traveled = self.current_speed * hours
        self.travelled_distance += distance_traveled

if __name__ == "__main__":
    new_car = Car(registration_number="ABC-123", maximum_speed=142)

    new_car.accelerate(30)
    new_car.accelerate(70)
    new_car.accelerate(50)

    print("Current Speed:", new_car.current_speed, "km/h")
    new_car.drive(1.5)
    print("Travelled Distance:", new_car.travelled_distance, "km")

#quiz 4

import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        if speed_change < 0:
            self.current_speed = max(0, self.current_speed + speed_change)
        else:
            self.current_speed = min(self.maximum_speed, self.current_speed + speed_change)

    def drive(self, hours):
        distance_traveled = self.current_speed * hours
        self.travelled_distance += distance_traveled

def print_car_properties(cars):
       print("{:<10} {:<15} {:<15} {:<15}".format("Car #", "Registration", "Max Speed (km/h)", "Distance (km)"))
       print("=" * 55)
       for car in cars:
          print("{:<10} {:<15} {:<15} {:<15}".format(car.registration_number, car.registration_number,car.maximum_speed, car.travelled_distance))

if __name__ == "__main__":
    cars = [Car(registration_number=f"ABC-{i + 1}", maximum_speed=random.randint(100, 200)) for i in range(10)]
    while all(car.travelled_distance < 10000 for car in cars):
        for car in cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)

            car.drive(1)
print_car_properties(cars)
