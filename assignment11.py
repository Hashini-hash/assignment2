#quiz1
class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"Publication: {self.name}")

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        super().print_information()
        print(f"Type: Book\nAuthor: {self.author}\nPage Count: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        super().print_information()
        print(f"Type: Magazine\nChief Editor: {self.chief_editor}")


def main():
    donald_duck_magazine = Magazine(name="Donald Duck", chief_editor="Aki Hyyppä")
    compartment_no_6_book = Book(name="Compartment No. 6", author="Rosa Liksom", page_count=192)


    donald_duck_magazine.print_information()
    print("\n--------------------------------\n")
    compartment_no_6_book.print_information()

if __name__ == "__main__":
    main()


#quiz 2

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.kilometers_driven = 0

    def drive(self, hours, speed):
        self.kilometers_driven += hours * speed

    def get_kilometers_driven(self):
        return self.kilometers_driven


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume



def main():
    electric_car = ElectricCar(registration_number="ABC-15", max_speed=180, battery_capacity=52.5)
    gasoline_car = GasolineCar(registration_number="ACD-123", max_speed=165, tank_volume=32.3)


    electric_car_speed = 150
    gasoline_car_speed = 140


    electric_car.drive(hours=3, speed=electric_car_speed)
    gasoline_car.drive(hours=3, speed=gasoline_car_speed)


    print(f"Electric Car Kilometers Driven: {electric_car.get_kilometers_driven()} km")
    print(f"Gasoline Car Kilometers Driven: {gasoline_car.get_kilometers_driven()} km")


if __name__ == "__main__":
    main()


