class Country:
    def __init__(self, capital, area, population):
        self.capital = capital
        self.area = area
        self.population = population

    def __str__(self):
        return f"{self.capital} - {self.area} км² - {self.population} человек"

countries = [
    Country("Минск", 207600, 9340000),
    Country("Берлин", 357592, 83200000),
    Country("Москва", 17100000, 143400000),
    Country("Париж", 551695, 67750000),
]

target_area = 1000000
print(f"Страны с площадью больше {target_area} км²:")
for country in countries:
    if country.area > target_area:
        print(country)

print()
target_population = 50000000
print(f"Страны с населением больше {target_population} человек:")
for country in countries:
    if country.population > target_population:
        print(country)

