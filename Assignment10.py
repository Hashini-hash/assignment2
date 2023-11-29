#quiz1

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, target_floor):
        # Move up or down to reach the target floor
        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moving up to floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moving down to floor {self.current_floor}")

if __name__ == "__main__":

    elevator = Elevator(bottom_floor=1, top_floor=10)
    elevator.go_to_floor(5)
    elevator.go_to_floor(1)

#quiz 2

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, target_floor):
        if target_floor < 1 or target_floor > self.top_floor:
            print("Invalid floor number")
            return

        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > 1:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_num, destination_floor):
        if 0 <= elevator_num < len(self.elevators):
            elevator = self.elevators[elevator_num]
            elevator.go_to_floor(destination_floor)
        else:
            print("Invalid elevator number")


def main():
    building = Building(bottom_floor=1, top_floor=10, num_elevators=3)


    building.run_elevator(elevator_num=0, destination_floor=7)


    building.run_elevator(elevator_num=1, destination_floor=3)


    building.run_elevator(elevator_num=2, destination_floor=9)


    building.run_elevator(elevator_num=0, destination_floor=1)

if __name__ == "__main__":
    main()

#Quiz 3

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, target_floor):
        if target_floor < 1 or target_floor > self.top_floor:
            print("Invalid floor number")
            return

        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > 1:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_num, destination_floor):
        if 0 <= elevator_num < len(self.elevators):
            elevator = self.elevators[elevator_num]
            elevator.go_to_floor(destination_floor)
        else:
            print("Invalid elevator number")

    def fire_alarm(self):
        print("Fire alarm activated! Moving all elevators to the bottom floor.")
        for elevator in self.elevators:
            elevator.go_to_floor(1)


def main():
    building = Building(bottom_floor=1, top_floor=10, num_elevators=3)


    building.run_elevator(elevator_num=0, destination_floor=7)


    building.run_elevator(elevator_num=1, destination_floor=3)


    building.run_elevator(elevator_num=2, destination_floor=9)


    building.fire_alarm()

if __name__ == "__main__":
    main()

#Quiz4


import random

class Car:
    def __init__(self, name, speed, fuel_efficiency):
        self.name = name
        self.speed = speed
        self.fuel_efficiency = fuel_efficiency
        self.distance_traveled = 0

    def drive(self, hours):
        distance = self.speed * hours
        fuel_consumed = distance / self.fuel_efficiency
        self.distance_traveled += distance
        return distance, fuel_consumed

    def __str__(self):
        return f"{self.name} - Distance: {self.distance_traveled:.2f} km"

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.uniform(-5, 5)
            car.speed += speed_change

            hours = 1
            distance, fuel_consumed = car.drive(hours)

            print(f"{car.name} drove {distance:.2f} km, consumed {fuel_consumed:.2f} liters of fuel.")

    def print_status(self):
        print("\nRace Status:")
        for car in self.cars:
            print(car)
        print("-----------------------")

    def race_finished(self):
        return any(car.distance_traveled >= self.distance for car in self.cars)


def main():
    #
    cars = [
        Car("Car1", speed=100, fuel_efficiency=10),
        Car("Car2", speed=120, fuel_efficiency=12),

    ]


    grand_derby = Race(name="Grand Demolition Derby", distance=8000, cars=cars)


    while not grand_derby.race_finished():
        grand_derby.hour_passes()


        if grand_derby.distance % 10 == 0:
            grand_derby.print_status()


    grand_derby.print_status()
    print("Race Finished!")

if __name__ == "__main__":
    main()
