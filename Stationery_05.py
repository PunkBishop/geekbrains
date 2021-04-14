class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки с {self.title} ручкой!")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки с {self.title} карандашом!")


class Marker(Stationery):
    def draw(self):
        print(f"Запуск отрисовки с {self.title} маркер!")


test_01 = Stationery('Тест')
test_01.draw()
test_02 = Pen("Тестовая ручка")
test_02.draw()
test_03 = Pencil("Тестовый карандаш")
test_03.draw()
test_04 = Marker("Тестовый маркер")
test_04.draw()