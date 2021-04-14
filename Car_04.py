class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Новая машина: {self.name} (цвет {self.color}), машина полицейская - {self.is_police}')

    def go(self):
        print(f'{self.name}: Машина начала движение.')

    def stop(self):
        print(f'{self.name}: Машина закончила движение.')

    def turn(self, direction):
        print(f'{self.name}: Машина повернула: {"налево" if direction == 0 else "направо"}.')

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}.'


class TownCar(Car):

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 60 else f"{self.name}: Скорость автомобиля: {self.speed}."


class WorkCar(Car):

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 40 else f"{self.name}: Скорость автомобиля: {self.speed}."


class SportCar(Car):

    pass


class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = PoliceCar('Лада', 'В полоску', 120)
police_car.go()
print(police_car.show_speed())
police_car.turn(1)
police_car.stop()
print()

work_car = WorkCar('Мерс', 'Белый', 60)
work_car.go()
work_car.turn(1)
print(work_car.show_speed())
work_car.stop()

print()
sport_car = SportCar('Ламба', 'Красный', 220)
sport_car.go()
sport_car.turn(1)
print(sport_car.show_speed())
sport_car.stop()
print()

town_car = TownCar('Смарт', 'Черный', 40)
town_car.go()
town_car.turn(1)
print(town_car.show_speed())
town_car.stop()

print(f'\nМашина {town_car.name} (цвет {town_car.color})')
print(f'Машина {police_car.name} (цвет {police_car.color})')
