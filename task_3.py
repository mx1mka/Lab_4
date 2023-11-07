class Transport:
    def __init__(self, city, distance, speed, cost):
        self.city = city
        self.distance = distance
        self.speed = speed
        self.cost = cost

    def get_time(self):
        return self.distance / self.speed

    def get_cost(self):
        return self.distance * self.cost

    def __str__(self):
        return f"{self.city} - {self.distance} км - {self.speed} км/ч - {self.cost} руб/км"

    def write_to_file(self, file_name):
        with open(file_name, "a", encoding="utf-8") as file:
            file.write(str(self) + "\n")

    def get_mode(self):
        return "Транспортное средство"

class Plane(Transport):
    def get_mode(self):
        return "Самолет"

class Train(Transport):
    def get_mode(self):
        return "Поезд"

class Car(Transport):
    def get_mode(self):
        return "Автомобиль"

transports = [
    Plane("Минск", 500, 800, 0.5),
    Train("Москва", 700, 100, 0.2),
    Car("Париж", 2000, 120, 0.3),
    Plane("Берлин", 1500, 900, 0.6),
    Train("Лондон", 1800, 80, 0.25)
]

file_name = "Транспорт.txt"
for transport in transports:
    transport.write_to_file(file_name)

fastest = None
cheapest = None
for transport in transports:
    if fastest is None or fastest.get_time() > transport.get_time():
        fastest = transport
    if cheapest is None or cheapest.get_cost() > transport.get_cost():
        cheapest = transport

print(f"Наиболее быстрое транспортное средство: {fastest.get_mode()} до {fastest.city} за {fastest.get_time()} часов")
print(f"Наиболее экономичное транспортное средство: {cheapest.get_mode()} до {cheapest.city} за {cheapest.get_cost()} рублей")
