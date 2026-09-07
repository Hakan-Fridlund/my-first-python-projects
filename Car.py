cars = []

# ToDo add function descriptions and protect code from invalid input
class Car:
    def __init__(
        self,
        brand,
        model,
        year,
        color,
        mileage,
        fuel_level,
        is_running,
        fuel_consumption,
        fuel_capacity,
    ):
        self.brand = brand
        self.model = model
        self.year = int(year)
        self.color = color
        self.mileage = max(0, float(mileage))
        self.fuel_level = max(0, float(fuel_level))
        self.is_running = bool(is_running)
        self.fuel_consumption = max(0.0001, float(fuel_consumption))
        self.fuel_capacity = max(1, float(fuel_capacity))

        if self.fuel_level >= self.fuel_capacity:
            self.fuel_level = self.fuel_capacity

    def __str__(self):
        return (
            f"Brand: {self.brand}\n"
            f"Model: {self.model}\n"
            f"Year: {self.year}\n"
            f"Color: {self.color}\n"
            f"Mileage: {self.mileage}\n"
            f"Fuel Level: {self.fuel_level}L\n"
            f"Fuel consumption:{self.fuel_consumption} litres per km\n"
            f"Max fuel capacity:{self.fuel_capacity} L"
        )

    def paint(self, color):
        if self.color == color:
            return f"The car is already: {color}"
        else:
            self.color = color
            return f"The car is now: {color}"

    def start(self):
        if self.is_running:
            return "Motor is already running"
        self.is_running = True
        return "Motor is now running"

    def stop(self):
        if not self.is_running:
            return "Motor is already off"
        self.is_running = False
        return "Motor is now off"

    def drive(self, distance):

        if distance <= 0:
            return "Distance needs to be greater than 0"

        if not self.is_running:
            return "Motor is not running, start your car."

        elif distance * self.fuel_consumption > self.fuel_level:
            return f"Cannot drive that far on your fuel, max distance is: {self.fuel_level / self.fuel_consumption} km"

        else:
            self.mileage += distance
            self.fuel_level = self.fuel_level - (distance * self.fuel_consumption)
            return f"You drove {distance} km, you have {self.fuel_level}L gas left."

    def refuel(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            return "invalid amount"

        if amount <= 0:
            return "The amount needs to be greater than 0"

        if self.fuel_level == self.fuel_capacity:
            return "The tank is already full"

        self.fuel_level += amount

        if self.fuel_level >= self.fuel_capacity:
            self.fuel_level = self.fuel_capacity
            return f"Tank is full ({self.fuel_level} L)."

        return f"Fuel level is now {self.fuel_level} L."

def get_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("\nError: the number must be greater than 0, try again: ")
                continue
            return value
        except ValueError:
            print("\nError: you need to type in a number, try again: ")


def get_year(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value < 1900 or value > 2026:
                print("\nError: the year needs to be from 1900 to 2026, try again: ")
                continue
            return value
        except ValueError:
            print("\nError: You must type in a number, try again: ")


def menu(car):
    while True:
        print("\n1. Change car")
        print("2. Paint")
        print("3. Start")
        print("4. Stop")
        print("5. Drive")
        print("6. Refuel")
        print("7. Print car")
        print("8. Exit")

        choice = input("Choice: ")
        match choice:
            case "1":
                car.brand = input("Please enter brand: ")
                car.model = input("Please enter model: ")
                car.year = get_year("Please enter year: ")
                car.color = input("Please enter color: ")
                car.mileage = get_float("Please enter mileage in km: ")
                car.fuel_level = get_float("Please enter fuel level in Litre: ")
                car.fuel_consumption = get_float("Please enter fuel consumption, Litres per km: ")
            case "2":
                car.color = input("Please enter color: ")
                print(f"\nThe car is now {car.color}")
            case "3":
                    print(car.start())
            case "4":
                print(car.stop())
            case "5":
                distance = get_float(f"You can drive for max: {car.fuel_level / car.fuel_consumption}km´s Please enter distance: ")
                print(car.drive(distance))
            case "6":
                amount = get_float(f"Your car has {car.fuel_level}L, and can tank {car.fuel_capacity - car.fuel_level} for a full tank\nPlease enter Litres to fuel: ")
                print(car.refuel(amount))
            case "7":
                print(f"\n{car}")
            case "8":
                break
            case _:
                print("\nPlease enter a valid choice 1-8")



def main():
    car = Car("Ford", "T-bird", "1950", "Red", 100, 40, False, 0.06, 100)
    menu(car)


if __name__ == "__main__":
    main()
