from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption  # только для 2 объектов


class Coat(Clothes):
    @property
    def consumption(self):
        print(f"Расход ткани на пошив пальто - {round(self.param / 6.5) + 0.5}")
        return round(self.param / 6.5) + 0.5  # для __add__


class Costume(Clothes):
    @property
    def consumption(self):
        print(f"Расход ткани на пошив костюма - {round(2 * self.param + 0.3) / 100}")
        return (2 * self.param + 0.3) / 100


coat = Coat(58)
costume = Costume(360)
print(coat + costume)